function [] = frequency(k, arr)
    set(0,'DefaultAxesFontSize',14,'DefaultAxesFontName','Times New Roman');
    set(0,'DefaultTextFontSize',14,'DefaultTextFontName','Times New Roman'); 
    figure('Units', 'normalized', 'OuterPosition', [0 0 1 1]);
    title('Относительная частота появления случайной величины');
    hold on;
    detX = 1 / k;
    N = hist(arr, k);
    N = N / (size(arr, 2) * detX);
    x = 0:1/k:1-1/k;
    bar(x, N);
    grid on;
end

