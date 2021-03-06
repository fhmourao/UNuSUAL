import sys
import os

##################################################################################################
### Functions
##################################################################################################

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

metrics_file = sys.argv[1]
dataset_file = sys.argv[2]
output_file = sys.argv[3]
binsize = float(sys.argv[4])
if binsize>1 or binsize<0 or binsize<0.01:
	print "Bin size is out of bounds. Please assign a real number from 0 to 1 greater than 0.01."
	exit(0)

##################################################################################################
### Reading the file
##################################################################################################

#Get the metrics for each user
user_unexpectedness_metrics = []
fin = open(metrics_file, "r")
for i in fin:
	i = i.rstrip()
	values = i.split(" ")
	user_unexpectedness_metrics += [[float(i) for i in values]]
fin.close()

#get the number of users who consumed each item
item_consumption = dict()
user_item = dict()
user_item_rating = dict()
user_dict = dict()
user_count = 1
fin = open(dataset_file, "r")
for i in fin:
	i.rstrip()
	values = i.split("\t")
	user = int(values[0])
	if user not in user_dict:
		user_dict[user] = user_count
		user_count += 1
	user = user_dict[user]
	item = int(values[1])
	rating = float(values[2])
	if user not in user_item:
		user_item[user] = []
		user_item_rating[user] = 0
	if item not in user_item[user]:
		user_item[user] += [item]
		user_item_rating[user] += rating
fin.close()

#calculate the average rating that each user gave to its items.
for user in user_item:
	user_item_rating[user] /= len(user_item[user])

##################################################################################################
### Calculating the popularity metric 
##################################################################################################

#calculating how many intervals there are
if 1%binsize==0:
	size_interval = int(1/binsize)
else:
	size_interval = int(1/binsize)+1

#creating a vector with the size of the intervals
unexpectedness_intervals = [[] for i in range(size_interval)]
count_unexpectedness_intervals = [[] for i in range(size_interval)]

#for each interval, create a vector with the size of the number of metrics
for i in range(len(unexpectedness_intervals)):
	unexpectedness_intervals[i] = [0 for j in range(len(user_unexpectedness_metrics[0]))]
	count_unexpectedness_intervals[i] = [0 for j in range(len(user_unexpectedness_metrics[0]))]

#for each user, passing through each metrics
for i in range(len(user_unexpectedness_metrics)):

	#for each unexpectedness metric of the user
	for j in range(len(user_unexpectedness_metrics[i])):

		#assigning the values to the correct intervals
		for k in range(size_interval):
			if user_unexpectedness_metrics[i][j]>=k*binsize and user_unexpectedness_metrics[i][j]<(k+1)*binsize:
				cont_position_interval = k
			elif user_unexpectedness_metrics[i][j]==1 and k==size_interval-1:
				cont_position_interval = k

		#summing to a interval x and metric j which is the average popularity
		unexpectedness_intervals[cont_position_interval][j] += user_item_rating[i+1]
		count_unexpectedness_intervals[cont_position_interval][j] += 1

#calculating the average. passing through each interval
for j in range(len(unexpectedness_intervals)):

	#passing though each metric
	for k in range(len(unexpectedness_intervals[j])):
		if count_unexpectedness_intervals[j][k]!=0:
			unexpectedness_intervals[j][k] /= count_unexpectedness_intervals[j][k]
		else:
			unexpectedness_intervals[j][k] = 0

##################################################################################################
### Printing and plotting
##################################################################################################

#printing results in a file
fout = open(output_file, "w")
initial_interval = 0
fout.write("Interval Metric1 Metric2 Metric3 Metric4 Metric5\n")
for i in range(len(unexpectedness_intervals)):
	end = initial_interval+binsize
	if end>1:
		end = 1
	fout.write(str(initial_interval)+"-"+str(end)+" ")
	initial_interval += binsize

	#passing through each metric and print its average popularity
	for j in range(len(unexpectedness_intervals[i])):
		if j+1!=len(unexpectedness_intervals[i]):
			fout.write(str(unexpectedness_intervals[i][j])+" ")
		else:
			fout.write(str(unexpectedness_intervals[i][j]))
	fout.write("\n")
fout.close()

#plotting results passing through all metrics
os.system("gnuplot -e \"datafile='"+output_file+"'; outputname='"+output_file[:-4]+".png'; columnplot="+str(j+2)+"\" gnuplot_averagerating.gp")
