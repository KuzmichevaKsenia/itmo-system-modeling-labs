function [] = correlation(arr, a, b)
    Dx = variance(arr);
    j = a:b;
    cor = zeros(size(j));
    cnt = 1;
    for i = j
        cor(cnt) = covariance(arr, i) / Dx;
        cnt = cnt + 1;
    end
    set(0,'DefaultAxesFontSize',14,'DefaultAxesFontName','Times New Roman');
    set(0,'DefaultTextFontSize',14,'DefaultTextFontName','Times New Roman'); 
    figure('Units', 'normalized', 'OuterPosition', [0 0 1 1]);
    title('√рафик корелл€ции');
    hold on;
    plot(j,cor,'r','LineWidth',3);
end

