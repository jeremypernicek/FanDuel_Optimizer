import time
import sys
import random

listDict = [
	{'Name':'Peyton Manning','Pos':'QB','Cost':9800,'Proj':25.754},
	{'Name':'Drew Brees','Pos':'QB','Cost':9500,'Proj':23.974},
	{'Name':'Colin Kaepernick','Pos':'QB','Cost':9200,'Proj':21.83},
	{'Name':'Matthew Stafford','Pos':'QB','Cost':8500,'Proj':21.82},
	{'Name':'Tom Brady','Pos':'QB','Cost':8500,'Proj':19.78},
	{'Name':'Tony Romo','Pos':'QB','Cost':7700,'Proj':19.246},
	{'Name':'Terrelle Pryor','Pos':'QB','Cost':6300,'Proj':18.952},
	{'Name':'Ryan Tannehill','Pos':'QB','Cost':6100,'Proj':15.932},
	{'Name':'Jake Locker','Pos':'QB','Cost':5400,'Proj':13.766},
	{'Name':'Christian Ponder','Pos':'QB','Cost':5300,'Proj':12.82},
	{'Name':'Chad Henne','Pos':'QB','Cost':5000,'Proj':8.114},
	{'Name':'Jason Campbell','Pos':'QB','Cost':5000,'Proj':7.71},
	{'Name':'Adrian Peterson','Pos':'RB','Cost':9500,'Proj':20.24},
	{'Name':'Marshawn Lynch','Pos':'RB','Cost':8300,'Proj':19.66},
	{'Name':'Trent Richardson','Pos':'RB','Cost':8000,'Proj':16.72},
	{'Name':'Chris Johnson','Pos':'RB','Cost':7800,'Proj':16.06},
	{'Name':'Frank Gore','Pos':'RB','Cost':6700,'Proj':15.11},
	{'Name':'Darren Sproles','Pos':'RB','Cost':7200,'Proj':14.29},
	{'Name':'Darren McFadden','Pos':'RB','Cost':7500,'Proj':13.18},
	{'Name':'Bernard Pierce','Pos':'RB','Cost':5900,'Proj':12.56},
	{'Name':'Stevan Ridley','Pos':'RB','Cost':6500,'Proj':12.19},
	{'Name':'Giovani Bernard','Pos':'RB','Cost':5700,'Proj':11.9},
	{'Name':'James Starks','Pos':'RB','Cost':5600,'Proj':10.69},
	{'Name':'Bilal Powell','Pos':'RB','Cost':4600,'Proj':10.18},
	{'Name':'Jimmy Graham','Pos':'TE','Cost':8000,'Proj':18.38},
	{'Name':'Tony Gonzalez','Pos':'TE','Cost':6800,'Proj':13.73},
	{'Name':'Jason Witten','Pos':'TE','Cost':6500,'Proj':13.42},
	{'Name':'Jordan Cameron','Pos':'TE','Cost':6400,'Proj':13.41},
	{'Name':'Jared Cook','Pos':'TE','Cost':6000,'Proj':12.77},
	{'Name':'Antonio Gates','Pos':'TE','Cost':5800,'Proj':12.76},
	{'Name':'Tyler Eifert','Pos':'TE','Cost':4900,'Proj':10.49},
	{'Name':'Charles Clay','Pos':'TE','Cost':4700,'Proj':7.54},
	{'Name':'Calvin Johnson','Pos':'WR','Cost':9000,'Proj':24.86},
	{'Name':'A.J. Green','Pos':'WR','Cost':8600,'Proj':20.9},
	{'Name':'Julio Jones','Pos':'WR','Cost':8200,'Proj':18.33},
	{'Name':'Randall Cobb','Pos':'WR','Cost':7800,'Proj':16.99},
	{'Name':'Andre Johnson','Pos':'WR','Cost':7300,'Proj':16.68},
	{'Name':'Pierre Garcon','Pos':'WR','Cost':7000,'Proj':15.33},
	{'Name':'Reggie Wayne','Pos':'WR','Cost':6800,'Proj':14.81},
	{'Name':'Steve Smith','Pos':'WR','Cost':6600,'Proj':14.53},
	{'Name':'Mike Wallace','Pos':'WR','Cost':6500,'Proj':14.44},
	{'Name':'Steve Johnson','Pos':'WR','Cost':6000,'Proj':13.58},
	{'Name':'Tavon Austin','Pos':'WR','Cost':5900,'Proj':13.23},
	{'Name':'DeAndre Hopkins','Pos':'WR','Cost':5700,'Proj':12.15},
	{'Name':'Josh Gordon','Pos':'WR','Cost':5500,'Proj':11.52},
	{'Name':'Nate Burleson','Pos':'WR','Cost':4900,'Proj':11.3},
	{'Name':'Eddie Royal','Pos':'WR','Cost':4500,'Proj':10},
	{'Name':'Steven Hauschka','Pos':'K','Cost':5000,'Proj':9},
	{'Name':'Seattle Seahawks','Pos':'D','Cost':5700,'Proj':15}
]
#create sub-lists by position of the players list
qbs = filter(lambda (d): d['Pos'] == 'QB', listDict)
rbs = filter(lambda (d): d['Pos'] == 'RB', listDict)
wrs = filter(lambda (d): d['Pos'] == 'WR', listDict)
tes = filter(lambda (d): d['Pos'] == 'TE', listDict)
ks = filter(lambda (d): d['Pos'] == 'K', listDict)
ds = filter(lambda (d): d['Pos'] == 'D', listDict)

	#takes a list of dicts (all players) and returns all possible lineups in the pattern:(qb,rb1,rb2,wr1,wr2,wr3,te1,k1,d1)	
def permutations(qbs,rbs,wrs,tes,ks,ds):
	possible_teams = []
	count = 0
	for qb1 in qbs:
		count += 1
		print count, qb1['Name']
		for rb1 in rbs:
			for rb2 in rbs:
				if rb2 != rb1:
					for wr1 in wrs:
						for wr2 in wrs:
							if wr2 != wr1:
								for wr3 in wrs:
									if wr3 != wr1 and wr3 != wr2:
										for te1 in tes:
											cost = qb1['Cost']+rb1['Cost']+rb2['Cost']+wr1['Cost']+wr2['Cost']+wr3['Cost']+te1['Cost']
											if cost < 50001:
												for k1 in ks:
													for d1 in ds:
														cost += k1['Cost'] + d1['Cost']
														if cost <= 60000:
															projected = qb1['Proj']+rb1['Proj']+rb2['Proj']+wr1['Proj']+wr2['Proj']+wr3['Proj']+te1['Proj']+k1['Proj']+d1['Proj']
															if projected > 105.3:
																cost_dict = {'ttl_Cost':cost}
																proj_dict = {'ttl_Proj':projected}
																team = [qb1, rb1, rb2, wr1, wr2, wr3, te1, k1, d1,cost_dict,proj_dict]
																if team not in possible_teams:
																	possible_teams.append(team)
	return possible_teams

#get a random sample of the player sub-lists	
def get_sample_of_position(list_to_sample, num_of_players_to_sample):
	players = []
	
	while len(players) < num_of_players_to_sample:
		player = list_to_sample[random.randint(0, len(list_to_sample)-1)]
		if player not in players:
			players.append(player)
	return players	
	
#perform the permutations function with a random sample of players, N times	
def perform_many_samples(num_of_samples, num_of_players):
	top_sampled_teams = []
	count = 0
	while count < num_of_samples:
		#filter player list by positions
		sample_of_qbs = get_sample_of_position(qbs,num_of_players)
		sample_of_rbs = get_sample_of_position(rbs,num_of_players)
		sample_of_wrs = get_sample_of_position(wrs,num_of_players)
		sample_of_tes = get_sample_of_position(tes,num_of_players)
		sample_of_ks = get_sample_of_position(ks,num_of_players)
		sample_of_ds = get_sample_of_position(ds,num_of_players)
		
		#create cartesian product
		this_sample = permutations(sample_of_qbs, sample_of_rbs, sample_of_wrs, sample_of_tes, sample_of_ks, sample_of_ds)
		#sort the list by ttl_Proj
		sorted_sample = sorted(this_sample, key=lambda k: k[10]['ttl_Proj'])
		#sort Descending
		sorted_sample.reverse()
		#append top projected team to top_sampled_teams
		if len(sorted_sample) > 0:
			top_sampled_teams.append(sorted_sample[0])
		
		count += 1
	return top_sampled_teams

def main():
	start_time = time.time()
	projected_filter = 115
	cost_filter = 60000
	num_of_samples_to_run = 10
	num_of_players_to_sample = 5
	
	if len(sys.argv) >= 2:
		projected_filter = int(sys.argv[1])
	else:
		projected_filter = 115
	print 'Projected_filter:', projected_filter
	
	if len(sys.argv) >= 3:
		num_of_samples_to_run = int(sys.argv[2])
	else:
		num_of_samples_to_run = 10
	print 'Running ', str(num_of_samples_to_run), ' samples'
	
	if len(sys.argv) >= 4:
		num_of_players_to_sample = int(sys.argv[3])
	else:
		num_of_players_to_sample = 5
	print 'Sampling ', num_of_players_to_sample, ' players','\n'
	
	#For the samples function: samples(# of samples, # of players), Don't sample more than 15 players!
	possible_teams = perform_many_samples(num_of_samples_to_run, num_of_players_to_sample)
	print '\n', str(len(possible_teams)) + ' possible teams created', '\n'
	sorted_teams = sorted(possible_teams, key=lambda k: k[10]['ttl_Proj'])
	sorted_teams.reverse()
	
	if len(sorted_teams) > 0:
		print 'The top projected team is: ', sorted_teams[0]
	else:
		print "No teams in list, adjust filters"
	
	#take top 100 teams
	top_slice = sorted_teams[:100]
	
	#write the top 100 items to a file named sampled_teams.json
	f = open('sampled_teams.txt', 'w')
	for team in top_slice:
		for player in team:
			print >> f, player
				
	f.close()
	print time.time() - start_time, "seconds to run entire program"
	
#Standard boilerplate template that calls the main() function.
if __name__ == '__main__':
	main()