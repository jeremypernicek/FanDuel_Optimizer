import time
import sys
import json

#list of all players to use in creating permutations
players = [
    {"Name":"Aaron Rodgers","Pos":"QB","Cost":9300,"Proj":22.3},
	{"Name":"Drew Brees","Pos":"QB","Cost":9600,"Proj":22.16},
	{"Name":"Tom Brady","Pos":"QB","Cost":8800,"Proj":19.7},
	{"Name":"Matt Ryan","Pos":"QB","Cost":8800,"Proj":19.65},
	{"Name":"Cam Newton","Pos":"QB","Cost":9200,"Proj":20.84},
	{"Name":"Adrian Peterson","Pos":"RB","Cost":9500,"Proj":18.36},
	{"Name":"Arian Foster","Pos":"RB","Cost":9100,"Proj":17.54},
	{"Name":"Doug Martin","Pos":"RB","Cost":9200,"Proj":16.88},
	{"Name":"Jamaal Charles","Pos":"RB","Cost":8800,"Proj":16.56},
	{"Name":"C.J. Spiller","Pos":"RB","Cost":8700,"Proj":15.91},
	{"Name":"Calvin Johnson","Pos":"WR","Cost":8800,"Proj":17.36},
	{"Name":"Brandon Marshall","Pos":"WR","Cost":7900,"Proj":15.51},
	{"Name":"A.J. Green","Pos":"WR","Cost":8100,"Proj":15.51},
	{"Name":"Dez Bryant","Pos":"WR","Cost":8300,"Proj":15.35},
	{"Name":"Julio Jones","Pos":"WR","Cost":8000,"Proj":14.64},
	{"Name":"Jimmy Graham","Pos":"TE","Cost":7500,"Proj":13.47},
	{"Name":"Rob Gronkowski","Pos":"TE","Cost":7100,"Proj":12.28},
	{"Name":"Jason Witten","Pos":"TE","Cost":6800,"Proj":10.83},
	{"Name":"Tony Gonzalez","Pos":"TE","Cost":6900,"Proj":10.8},
	{"Name":"Vernon Davis","Pos":"TE","Cost":6600,"Proj":9.51},
	{"Name":"Stephen Gostkowski","Pos":"K","Cost":5400,"Proj":8.78},
	{"Name":"Phil Dawson","Pos":"K","Cost":5400,"Proj":8.59},
	{"Name":"Matt Bryant","Pos":"K","Cost":5300,"Proj":8.48},
	{"Name":"Blair Walsh","Pos":"K","Cost":5100,"Proj":8.22},
	{"Name":"Garrett Hartley","Pos":"K","Cost":5300,"Proj":7.91},
	{"Name":"San Francisco 49ers","Pos":"D","Cost":5400,"Proj":14.06},
	{"Name":"Seattle Seahawks","Pos":"D","Cost":5700,"Proj":13.69},
	{"Name":"Houston Texans","Pos":"D","Cost":5500,"Proj":12.38},
	{"Name":"Chicago Bears","Pos":"D","Cost":5500,"Proj":12},
	{"Name":"Pittsburgh Steelers","Pos":"D","Cost":5000,"Proj":11.5}
]

#takes a list of all players and returns all possible lineups in the pattern:(qb,rb1,rb2,wr1,wr2,wr3,te1,k1,d1)	
def permutations(list_of_players, filter_by_cost, filter_by_projection):
	possible_teams = []
	
	#create sub-lists by position of the players list
	qbs = filter(lambda (d): d['Pos'] == 'QB', players)
	rbs = filter(lambda (d): d['Pos'] == 'RB', players)
	wrs = filter(lambda (d): d['Pos'] == 'WR', players)
	tes = filter(lambda (d): d['Pos'] == 'TE', players)
	ks= filter(lambda (d): d['Pos'] == 'K', players)
	ds= filter(lambda (d): d['Pos'] == 'D', players)
	
	for qb1 in qbs:
		print qb1['Name']
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
											if cost < filter_by_cost - 9999:
												for k1 in ks:
													for d1 in ds:
														cost += k1['Cost'] + d1['Cost']
														if cost <= filter_by_cost:
															projected = qb1['Proj']+rb1['Proj']+rb2['Proj']+wr1['Proj']+wr2['Proj']+wr3['Proj']+te1['Proj']+k1['Proj']+d1['Proj']
															if projected > filter_by_projection:
																cost_dict = {'ttl_Cost':cost}
																proj_dict = {'ttl_Proj':projected}
																team = [qb1, rb1, rb2, wr1, wr2, wr3, te1, k1, d1,cost_dict,proj_dict]
																if team not in possible_teams:
																	possible_teams.append(team)
	return possible_teams
	
def main():
	start_time = time.time()
	projected_filter = 115
	cost_filter = 60000
	
	if len(sys.argv) >= 2:
		projected_filter = int(sys.argv[1])
	else:
		projected_filter = 115
	print 'Projected_filter:', projected_filter
		
	if len(sys.argv) >= 3:
		file_name = sys.argv[2]
	else:
		file_name = 'max_projected_teams'
	
	if len(sys.argv) >= 4:
		cost_filter = int(sys.argv[3])
	else:
		cost_filter = 60000
	print 'Cost_filter:', cost_filter, '\n'

	
	possible_teams = permutations(players,cost_filter,projected_filter)
	print '\n', str(len(possible_teams)) + ' possible teams created', '\n'
	sorted_teams = []
	if len(possible_teams) > 0:
		sorted_teams = sorted(possible_teams, key=lambda k: k[10]['ttl_Proj'])
		sorted_teams.reverse()
		print 'The top projected team is:'
		for player in sorted_teams[0]:
			print player
	else:
		print 'No teams returned, adjust filters'
		
	top_slice = sorted_teams[:100]
	
	#print .json data
	with open(file_name+'.json', 'w') as outfile:
		json.dump(top_slice, outfile)
	
	#print the top 100 items in readable format
	f = open(file_name+'.txt', 'w')
	for team in top_slice:
		for player in team:
			print >> f, player
	f.close()
	print time.time() - start_time, "seconds to run entire program"
	
#Standard boilerplate template that calls the main() function.
if __name__ == '__main__':
	main()