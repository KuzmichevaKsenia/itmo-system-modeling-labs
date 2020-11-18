function [Mx] = expectedValue(arr)
    Mx = sum(arr) /  size(arr, 2);
end