function [] = scatterPlot(arr)
    set(0,'DefaultAxesFontSize',14,'DefaultAxesFontName','Times New Roman');
    set(0,'DefaultTextFontSize',14,'DefaultTextFontName','Times New Roman'); 
    figure('Units', 'normalized', 'OuterPosition', [0 0 1 1]);
    title('Диаграмма рассеяния');
    hold on;
    for i = 1:size(arr, 2) - 1
        plot(arr(i), arr(i + 1),'r*');
    end
    grid on;
end

