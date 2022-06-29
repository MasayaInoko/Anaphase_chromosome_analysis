T = readtable('211116_escape nuc area_analysis test.csv');
DATA = [T.x_nuc1 T.y_nuc1 T.z_nuc1 T.time_flame];
%INDEX = find(DATA(:,5)==1);
%EXT_DATA = DATA(INDEX,:);

v = VideoWriter('test_nuc.avi');
open(v);
k = 1;
%LAST_FRAME = EXT_DATA(end,4);
LAST_FRAME = DATA(end,4);
F(LAST_FRAME) = struct('cdata',[],'colormap',[]);
for i = 1:LAST_FRAME
  %IND(i).LINE = find(EXT_DATA(:,4) == i);
  IND(i).LINE = find(DATA(:,4) == i);
  [NUM ~] = size(IND(i).LINE);
  %IND(i).COORDINATES = EXT_DATA(k:k+NUM-1,:);
  IND(i).COORDINATES = DATA(k:k+NUM-1,:);
  k = k + NUM;
  figure;
  plot3(IND(i).COORDINATES(:,1),IND(i).COORDINATES(:,2),IND(i).COORDINATES(:,2),'o');hold on;
  axis([0 100 0 100 0 100]);grid on;
  F(i) = getframe;
  writeVideo(v,F(i));
  close;
end
close(v);
movie(F);
