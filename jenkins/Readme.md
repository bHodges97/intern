benchmarkmockup.sh creates random numbers for input and out put
benchmarkstats.sh stores the numbers into the csv file that is then plotted in jenkins

config.xml is the dashboard config, it goes in the jenkins install directory
jobs/config.xml is the job (build/test) config file, it goes in the project folder in the jenkins job directory.

Jenkins plugins needed:
Dashboard view
Performance plugin
Plot plugin
XUnit plugin
