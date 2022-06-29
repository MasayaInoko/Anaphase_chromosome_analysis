%% This program calculate least square plane from xyz dots

%%  parameters for the size of the plane
sizeP_X = 30;
sizeP_Y = 30;

%% for multiple files
FileList = dir('*.csv');
FileNum = size(FileList,1);
%savename = [FileList(i).name]

%rootname = 'file';

for i = 1:FileNum 
  
%%  read xyz coordinates
xyz = readtable(FileList(i).name);
rootname = [FileList(i).name];
csvextension = '.csv';
figextension = '.fig';
%load XYZ;

%%  calculate the center of mass
%Xmass = mean(XYZ(:,1));
%Ymass = mean(XYZ(:,2));
%Zmass = mean(XYZ(:,3));
Xmass = mean(xyz.Var1(:));
Ymass = mean(xyz.Var2(:));
Zmass = mean(xyz.Var3(:));

%%  calculate principle components
XYZ = [xyz.Var1(:), xyz.Var2(:), xyz.Var3(:)];
PCA_XYZ = pca(XYZ);

%% select the third PCA verctor as normal vector
PCA_3X = PCA_XYZ(1,3);
PCA_3Y = PCA_XYZ(2,3);
PCA_3Z = PCA_XYZ(3,3);


%% calculate centrosome-plane distance
Dis1 = abs(PCA_3X*xyz{1,1} + PCA_3Y*xyz{1,2} + PCA_3Z*xyz{1,3} - (PCA_3X*Xmass + PCA_3Y*Ymass + PCA_3Z*Zmass))/sqrt(PCA_3X^2+PCA_3Y^2+PCA_3Z^2);
Dis2 = abs(PCA_3X*xyz{2,1} + PCA_3Y*xyz{2,2} + PCA_3Z*xyz{2,3} - (PCA_3X*Xmass + PCA_3Y*Ymass + PCA_3Z*Zmass))/sqrt(PCA_3X^2+PCA_3Y^2+PCA_3Z^2);
Dis3 = abs(PCA_3X*xyz{3,1} + PCA_3Y*xyz{3,2} + PCA_3Z*xyz{3,3} - (PCA_3X*Xmass + PCA_3Y*Ymass + PCA_3Z*Zmass))/sqrt(PCA_3X^2+PCA_3Y^2+PCA_3Z^2);
Dis4 = abs(PCA_3X*xyz{4,1} + PCA_3Y*xyz{4,2} + PCA_3Z*xyz{4,3} - (PCA_3X*Xmass + PCA_3Y*Ymass + PCA_3Z*Zmass))/sqrt(PCA_3X^2+PCA_3Y^2+PCA_3Z^2);
Dis_Sum = Dis1 + Dis2 + Dis3 + Dis4;

PCA_XYZ = [PCA_3X PCA_3Y PCA_3Z Xmass Ymass Zmass Dis1 Dis2 Dis3 Dis4 Dis_Sum];
csvfilename = [rootname, csvextension]; 
writematrix(PCA_XYZ, csvfilename)


%%  derive the plane
for simX = 1:sizeP_X
  for simY = 1:sizeP_Y
    simZ(simY,simX) = Zmass - (PCA_3X*(simX - Xmass))./PCA_3Z - (PCA_3Y*(simY - Ymass))./PCA_3Z;
  end

  
end

%%  visualize the derived plane and the dots
figure;surf(simZ);hold on;
fig = plot3(xyz.Var1(:),xyz.Var2(:),xyz.Var3(:),'o');
%data = 2*i;
%filename = [rootname, num2str(i), extension];
figfilename = [rootname, figextension];
savefig(figfilename) 
%str = [fig.name]
%movefile(,savename);

%savefig(fig, );
%plot3(XYZ(:,1),XYZ(:,2),XYZ(:,3),'o');
%plot3(Xmass,Ymass,Zmass,'ro');

FILE_OUT = sprintf('NormalVect%d',i);
%FILE_OUT_C = char(FILE_OUT);
save(FILE_OUT,'PCA_XYZ');
close
end