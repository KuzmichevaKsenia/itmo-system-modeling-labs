function [Dx] = variance(arr)
    sum = 0;
    n = size(arr, 2);
    Mx = expectedValue(arr);
    for i = 1:n
        sum = sum + (arr(i) - Mx) ^ 2;
    end
    Dx = sum / (n - 1);
end

