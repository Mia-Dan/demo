clear; close; clc;

%% LOAD DATA & PREPROCESSING
imgs = loadMNISTImages('./mnist/train-images-idx3-ubyte');
% labels = loadMNISTLabels('./mnist/train-labels-idx1-ubyte');
imgs = imresize(imgs,[64 64]);
imgs = reshape(imgs,64,64,1,[]);
% a = imgs(:,:,1,1), imshow(a) % Test OK

[~,~,~,N_imgs] = size(imgs);
imgsn = single(imgs)*2 - 1; % normalization for the following network

%% DEFINE GENERATOR NETWORK
% Define a network that generates images from 1-by-1-by-100 arrays of random values. 
filterSize = [4 4];
numFilters = 64;
numLatentInputs = 100;

layersGenerator = [
    imageInputLayer([1 1 numLatentInputs],'Normalization','none','Name','in')
    
    transposedConv2dLayer(filterSize,8*numFilters,'Name','tconv1')
    batchNormalizationLayer('Name','bn1')
    reluLayer('Name','relu1')
    
    transposedConv2dLayer(filterSize,4*numFilters,'Stride',2,'Cropping',1,'Name','tconv2')
    batchNormalizationLayer('Name','bn2')
    reluLayer('Name','relu2')
    
    transposedConv2dLayer(filterSize,2*numFilters,'Stride',2,'Cropping',1,'Name','tconv3')
    batchNormalizationLayer('Name','bn3')
    reluLayer('Name','relu3')
    
    transposedConv2dLayer(filterSize,numFilters,'Stride',2,'Cropping',1,'Name','tconv4')
    batchNormalizationLayer('Name','bn4')
    reluLayer('Name','relu4')

    % Specify 1 filter which correspond to the intensity channel of the generated images.
    % If for RGB picture, 3 filters.
    transposedConv2dLayer(filterSize,1,'Stride',2,'Cropping',1,'Name','tconv5')
    tanhLayer('Name','tanh')];

lgraphGenerator = layerGraph(layersGenerator);
% To train the network with a custom training loop and enable automatic differentiation, 
% convert the layer graph to a dlnetwork object.
dlnetGenerator = dlnetwork(lgraphGenerator)

%% DEFINE DISCRIMINATOR NETWORK

scale = 0.2;

layersDiscriminator = [
%     imageInputLayer([64 64 3],'Normalization','none','Name','in')
    imageInputLayer([64 64 1],'Normalization','none','Name','in')
    
    convolution2dLayer(filterSize,numFilters,'Stride',2,'Padding',1,'Name','conv1')
    leakyReluLayer(scale,'Name','lrelu1')
    
    convolution2dLayer(filterSize,2*numFilters,'Stride',2,'Padding',1,'Name','conv2')
    batchNormalizationLayer('Name','bn2')
    leakyReluLayer(scale,'Name','lrelu2')
    
    convolution2dLayer(filterSize,4*numFilters,'Stride',2,'Padding',1,'Name','conv3')
    batchNormalizationLayer('Name','bn3')
    leakyReluLayer(scale,'Name','lrelu3')
    
    convolution2dLayer(filterSize,8*numFilters,'Stride',2,'Padding',1,'Name','conv4')
    batchNormalizationLayer('Name','bn4')
    leakyReluLayer(scale,'Name','lrelu4')
    
    convolution2dLayer(filterSize,1,'Name','conv5')];

lgraphDiscriminator = layerGraph(layersDiscriminator);

dlnetDiscriminator = dlnetwork(lgraphDiscriminator)
% Visualize The Generator And Discriminator Networks In A Plot
figure
subplot(1,2,1), plot(lgraphGenerator), title("Generator")
subplot(1,2,2), plot(lgraphDiscriminator), title("Discriminator")

%% DEFINE MODEL GRADIENTS AND LOSS FUNCTIONS
% Those are defined in seperate functions.

%% SPECIFY TRAINING OPTIONS
numEpochs = 1000;
miniBatchSize = 128;
% augimds.MiniBatchSize = miniBatchSize;

learnRateGenerator = 0.0002;
learnRateDiscriminator = 0.0001;

trailingAvgGenerator = [];
trailingAvgSqGenerator = [];
trailingAvgDiscriminator = [];
trailingAvgSqDiscriminator = [];

gradientDecayFactor = 0.5;
squaredGradientDecayFactor = 0.999;

%% TRAIN MODEL

% visualization during training process
ZValidation = randn(1,1,numLatentInputs,64,'single');
dlZValidation = dlarray(ZValidation,'SSCB'); % 'SSB' (spatial, spatial, batch), 'SSCB' (spatial, spatial, channel, batch)

% train initialization
figure
iteration = 0;
start = tic;

% Loop over epochs.
%% TO "Resume" Training Process, Run This Section. (Saved .mat File Required)

for i = 1:numEpochs
    
%    Reset and shuffle datastore.
%    reset(augimds);
%    augimds = shuffle(augimds);
    seq = randperm(N_imgs);
    mark1 = 0; % mark the last used image

%    Loop over mini-batches.
%    while hasdata(augimds)
    while (mark1 + miniBatchSize <= N_imgs)  
        
        % Read mini-batch of data.
        X = imgsn(:,:,:,seq(mark1+1:mark1+miniBatchSize));
        % size(imgsn);
%         data = read(augimds);
        
        % Ignore last partial mini-batch of epoch.
%         if size(data,1) < miniBatchSize
%             continue
%         end
        
        % Concatenate mini-batch of data and generate latent inputs for the
        % generator network.
        Z = randn(1,1,numLatentInputs,size(X,4),'single');

        % Normalize the images
        % data = single(data)*2 - 1;
        
        % Convert mini-batch of data to dlarray specify the dimension labels
        % 'SSCB' (spatial, spatial, channel, batch).
        dlX = dlarray(X, 'SSCB');
        dlZ = dlarray(Z, 'SSCB');
        
        % Evaluate the model gradients and the generator state using
        % dlfeval and the modelGradients function listed at the end of the
        % example.
        [gradientsGenerator, gradientsDiscriminator, stateGenerator] = ...
            dlfeval(@modelGradients, dlnetGenerator, dlnetDiscriminator, dlX, dlZ);
        dlnetGenerator.State = stateGenerator;
        % ERROR! Layer 'in': Invalid input data. Layer input must have one channel dimension labeled 'C'.

        % Update the discriminator network parameters.
        [dlnetDiscriminator.Learnables,trailingAvgDiscriminator,trailingAvgSqDiscriminator] = ...
            adamupdate(dlnetDiscriminator.Learnables, gradientsDiscriminator, ...
            trailingAvgDiscriminator, trailingAvgSqDiscriminator, iteration, ...
            learnRateDiscriminator, gradientDecayFactor, squaredGradientDecayFactor);
        
        % Update the generator network parameters.
        [dlnetGenerator.Learnables,trailingAvgGenerator,trailingAvgSqGenerator] = ...
            adamupdate(dlnetGenerator.Learnables, gradientsGenerator, ...
            trailingAvgGenerator, trailingAvgSqGenerator, iteration, ...
            learnRateGenerator, gradientDecayFactor, squaredGradientDecayFactor);
        
        % Every 100 iterations, display batch of generated images using the
        % held-out generator input.
        if mod(iteration,100) == 0 || iteration == 1
            
            % Generate images using the held-out generator input.
            dlXGeneratedValidation = predict(dlnetGenerator,dlZValidation);
            
            % Rescale the images in the range [0 1] and display the images.
            I = imtile(extractdata(dlXGeneratedValidation));
            I = rescale(I);
            imshow(I)
            
            % Update the title with training progress information.
            D = duration(0,0,toc(start),'Format','hh:mm:ss');
            title(...
                "Epoch: " + i + ", " + ...
                "Iteration: " + iteration + ", " + ...
                "Elapsed: " + string(D))
            
            drawnow
        end
        mark1 = mark1 + miniBatchSize;  
        iteration = iteration + 1;   
    end
end

%% GENERATE NEW IMAGES
ZNew = randn(1,1,numLatentInputs,16,'single');
dlZNew = dlarray(ZNew,'SSCB');
% generate new images
dlXGeneratedNew = predict(dlnetGenerator,dlZNew);
% display
I = imtile(extractdata(dlXGeneratedNew));
I = rescale(I);
% image(I)
imshow(I)
title("Generated Images")




