T = readtable('211116_1_Pos3_2.tif.csv');
DATA = [T.X T.Y T.Slice T.Frame T.check];
INDEX = find(DATA(:,5)==1);
EXT_DATA = DATA(INDEX,:);

v = VideoWriter('test.avi');
open(v);
k = 1;
LAST_FRAME = EXT_DATA(end,4);
F(LAST_FRAME) = struct('cdata',[],'colormap',[]);
for i = 1:LAST_FRAME
  IND(i).LINE = find(EXT_DATA(:,4) == i)
  [NUM ~] = size(IND(i).LINE);
  IND(i).COORDINATES = EXT_DATA(k:k+NUM-1,:);
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
