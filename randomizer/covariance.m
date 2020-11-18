function [Kj] = covariance(arr, j)
    n = size(arr, 2);
    Mx = expectedValue(arr);
    sum = 0;
    for i = 1:n - j
        sum = sum + (arr(i) - Mx) * (arr(i + j) - Mx);
    end
    Kj = sum / (n - j);
end

