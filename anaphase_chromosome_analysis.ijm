AO = 14 //毎回該当する細胞のAO時点を記入する

showMessage("Select Save Folder");
saveDir = getDirectory("Choose a Directory");
f = File.open(saveDir+"nuc_coordinates.csv");

run("Duplicate...", "duplicate");
run("Set Measurements...", "area mean centroid integrated stack redirect=None decimal=3");
run("Set Scale...", "distance=4.5 known=1 pixel=1 unit=µm global");
d = getTitle();

Stack.getDimensions(width, height, channels, slices, frames);

Stack.setChannel(2);
Stack.setFrame(AO);
run("Make Substack...", "slices=1-"+slices+" frames="+AO);
run("Split Channels");
rename("AO_H2B");
n = 1;
for (j = 1; j < slices+1; j++) {
	selectWindow("AO_H2B");
	run("Duplicate...", "duplicate");
	setSlice(n); 	
	run("Gaussian Blur...", "sigma=2 stack");
	setAutoThreshold("Otsu dark");
	run("Analyze Particles...", "size=10-Infinity show=Outlines display clear include slice");
	//results = nResults;
	//for (i = 0; i < results; i++) {
	//getResults = getResult("Area" "Mean" "X" "Y" "IntDen" "RawIntDen" "Slice", i);
	//print(getResults);
	//print(f,getResults + "\t"); 
    n = n+1;
  }
File.close(f);
