data = importdata('irisdataset.mat');

% ������
irisdata2 = irisdata(1:100,1:4); 
kind2 = kind(1:100,1);
for i = 1:100
    if(kind2(i,1) == 1) stddata2(i,:) = [irisdata2(i,:) 1]; % ȡΪSetosa������
    else stddata2(i,:) = [-1.*irisdata2(i,:) -1];          % ȡVersicolorΪ������
    end
end

w = ones(5,1);   % ��ʼ��w
p = 1;           % ѧϰ���� = 1

k = 1; i = 0;    
while (i<100)   
    if(stddata2(k,:)*w > 0) i=i+1;
    else w = w + p .* stddata2(k,:)'; i=0;
    end
    k = mod(k,100)+1;
    
% ���� for(n = 1:100)
%    ���и��£���flag��Ϊ1
%    ��������Ϊ0����ﵽ����
%    ���ܸ������Ķ�
    
end  % һ�����ڣ�100�Σ�δ�ı� w����ʱwΪ����
disp(w')


