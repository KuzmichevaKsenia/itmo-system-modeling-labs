function [randomArray] = generator(n)
    randomArray = zeros(1, n);
    a = 630360016;
    m = 2147483647;
    xsi = 1148216685;
    for i = 1:n
        randomArray(i) = xsi / m;
        xsi = mod(a * xsi, m);
    end
end