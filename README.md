# DigitalEpidemilogySimulation

DIGITAL EPIDEMIOLOGY
ASSIGNMENT #1
DUE DATE: DECEMBER 22nd, 2017
HARD DEADLINE: DECEMBER 29th, 2017
========================================================

* PART 1: EPIDEMIC PROCESS ON A SOCIAL NETWORK (8 points)

	1.1 - Consider either a synthetic Barabasi-Albert graph or a real social network (e.g., from the SNAP http://snap.stanford.edu/ or Konect http://konect.uni-koblenz.de/ repositories). If the chosen graph has multiple disconnected components, select the largest connected component. Make sure the graph has at least a few thousand nodes. Compute and plot the degree distribution.

	1.2 - Set up a simulation of an SIR epidemic process on the graph. Start the epidemic from a randomly chosen node. Choose values of model parameters \beta and \mu that allow the epidemic to take off with high probability, reaching most of the nodes.

	1.3 -  Plot epidemic curves for multiple stochastic realizations of the epidemic. Compute the probability distribution of the overall attack rate (number of recovered nodes at the end of the simulation / total number of nodes) and the probability distribution of peak times for the epidemic. Display these distributions using boxplots.


* PART 2: VACCINATION AND HERD IMMUNITY (10 points)

	2.1 - Modify the simulation above so that it supports a given initial fraction r of randomly chosen "immunized" nodes, i.e., nodes that cannot be infected. Can you provide an upper bound for the overall attack rate without having to simulate the epidemic?

	2.2 - For a range of values of the initial fraction of immunized nodes (e.g., r = 0.01, 0.1, 0.5, 0.8, 0.9, ...) simulate the SIR epidemic above (multiple realizations for each value of r) and plot the overall attack rate as a function of the fraction r of immunized nodes.

	2.3 - Generate a random Erdős–Rényi graph with the same size and density as the original social network. Repeat the experiment 2.2 above. Compare the results you obtain in this case and in the previous case, and explain the differences you observe.


* PART 3: TARGETED VACCINATION STRATEGIES (12 points)

	3.1 - Imagine that you have a "budget" of M vaccination doses, with M < N, where N is the size of your network. That is, you can immunize a fraction r = M/N of nodes. You have studied above the effect of randomly immunizing the network nodes. Can you improve the performance of immunization, in terms of reduced overall attack rate, by means of "targeted" immunization? That is, by choosing the nodes to be immunized according to some specific strategy rather than choosing them at random. Provide an example of such a strategy, and test it in simulation, comparing the results you obtain with those of Part 2.2.

	3.2 - Now imagine that you still have a limited budget of M vaccination doses, but you cannot use information about the graph to decide how to use it. You can simulate a certain number of epidemics, without immunization, and use "historical" information on which nodes are infected (and when, and how often) to define your targeted immunization strategy. Design such a strategy and show its performance in simulation, comparing it to the random immunization of Part 2.2 and the targeted strategy you devised in Part 3.1 above.

	3.3 - Finally, imagine that you have limited information about the social network: you are given a set of K nodes (K << N, say K ~ 10% of the network) and for those K nodes you are given a list of their neighbors. Design a targeted immunization strategy that makes use of this information, and test its performance in simulation.


* BONUS points (max 5 bonus points overall):

	- nicely commented code with accurately discussed results (3 points)

	- timely completion of the assignment by due date of December 18th (2 points)

	- assignment provided as a single self-contained Jupyter Notebook (2 points)


NOTES:
	- you can use any programming language(s) you like
