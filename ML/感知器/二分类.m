data = importdata('irisdataset.mat');

% 用感知器算法实现二分类
irisdata2 = irisdata(1:100,1:4); 
kind2 = kind(1:100,1);
for i = 1:100
    if(kind2(i,1) == 1) stddata2(i,:) = [irisdata2(i,:) 1]; % 取为Setosa正样本
    else stddata2(i,:) = [-1.*irisdata2(i,:) -1];           % 取Versicolor为负样本。这里仅选取这两类进行二分类。
    end
end

w = ones(5,1);   % 初始化w
p = 1;           % 学习步长 = 1

k = 1; i = 0;    
while (i<100)    % 遍历所有样本（连续100次）w都能正确进行分类，则此时w为所求

    if(stddata2(k,:)*w > 0) i=i+1;
    else w = w + p .* stddata2(k,:)'; i=0;
    end
    k = mod(k,100)+1;   % 每轮循环结束，k+1；当k = 100时，重置为1进入下一轮。
    
% 或者 for(n = 1:100)
%    若有更新，则flag变为1
%    若结束仍为0，则达到最优
%    可能更便于阅读
    
end  % 一个周期（100次）未改变 w，此时w为所求
disp(w')


