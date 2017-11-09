%% Intialize necessary variables
x_pixel = 1:3647;
x_pixel = x_pixel';

%% Calibration of wavelengths & pixel mapping

calibration_data = xlsread('CalibrationAnalysis.xlsx');
red_spec = calibration_data(2:end,3);
yellow_spec = calibration_data(2:end,2);
%green_spec = calibration_data(:,2);
blue_spec = calibration_data(2:end,1);

wavelength = -0.0798.*(x_pixel) + 688.35;
red_smooth = smooth(red_spec,50);
yellow_smooth = smooth(yellow_spec,50);
%green_smooth = smooth(green_spec,50);
blue_smooth = smooth(blue_spec,50);


figure();
plot(wavelength, red_smooth, 'r');
hold on
%plot(wavelength, green_smooth,'g');
plot(wavelength, yellow_smooth,'y');
plot(wavelength, blue_smooth,'b');
xlabel('Wavelength (nm)');
ylabel('Pixel Intensity');
legend('Red','Yellow','Blue'); 
%legend('Red','Green','Yellow','Blue'); 
set(gcf,'color','w');

%% Flourescein Dynamic Range Analysis with Variale Concentrations
% Concentrations tested 1uM, 3uM, 10uM, 30uM, 90uM
fluorescein_data = xlsread('Fluorescein_Conc_Analysis.xlsx');

spec_90uM = fluorescein_data(:,1);
spec_30uM = fluorescein_data(:,2);
spec_10uM = fluorescein_data(:,3);
spec_3uM = fluorescein_data(:,4);
spec_1uM = fluorescein_data(:,5);

spec_90uM_smooth = smooth(spec_90uM,50);
spec_30uM_smooth = smooth(spec_30uM,50);
spec_10uM_smooth = smooth(spec_10uM,50);
spec_3uM_smooth = smooth(spec_3uM,50);
spec_1uM_smooth = smooth(spec_1uM,50);

figure();
plot(wavelength, spec_90uM_smooth, 'k');
hold on
plot(wavelength, spec_30uM_smooth,'r');
plot(wavelength, spec_10uM_smooth,'y');
plot(wavelength, spec_3uM_smooth,'g');
plot(wavelength, spec_1uM_smooth,'b');
xlabel('Wavelength (nm)');
ylabel('Pixel Intensity');
legend('90uM','30uM','10uM','3uM','1uM'); 
set(gcf,'color','w');

%% Rhodamine & Fluorescein Emission Spectrum Analysis
fluorescein_data = xlsread('Fluorescein_Conc_Analysis.xlsx');
rhodamine_data = xlsread('Rhodamine_Conc_Analysis.xlsx');

fluor_30uM = fluorescein_data(:,2);
rhod_30uM = rhodamine_data(:,1);

fluor_30uM_smooth = smooth(fluor_30uM,50);
rhod_30uM_smooth = smooth(rhod_30uM,50);

figure();
plot(wavelength, fluor_30uM_smooth, 'g');
hold on
plot(wavelength(3:end), rhod_30uM_smooth(3:end)-12, 'y');
xlabel('Wavelength (nm)');
ylabel('Pixel Intensity');
set(gcf,'color','w');