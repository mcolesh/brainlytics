%% show images of the frames 50-80 
mean_cond4 = mean(cond4,3)-1;


mimg(mean_cond4(:,50:80), 100,100, -2e-3,2e-3); %colormap(jet); 
colormap(mapgeog);

mean_cond4_timecourse = mean(mean_cond4,1);

%% plot the signal strength over the time course of 530ml after frame 27 (frame zero)
time_axis = (([1:80] - 27)*10);
figure();
plot(time_axis, mean_cond4_timecourse(1:80));


%% masking
figure(100);
mimg(mean_cond4(:,35), 100,100, 0, 5e-4); %colormap(jet); 
colormap(mapgeog);
myFirstRoi = choose_polygon(100);

%% plotting masked frames
signal_timecourse = mean(mean_cond4(myFirstRoi,:),1);

figure();
plot(signal_timecourse(2:80));






