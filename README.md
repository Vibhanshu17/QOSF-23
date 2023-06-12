This repo contains the work done under the QOSF Mentorship program (Cohort #7) during April-June, 2023. \
My team consists of [Jacob Vaknin](https://www.linkedin.com/in/kobevaknin/) and [Sanaa Agarwal](https://www.linkedin.com/in/sanaa-agarwal-837596106/) under the mentorship of [Vesselin Gueorguiev](https://www.linkedin.com/in/vgg-consulting/).

# Heterogenous Vehicle Routing
The [Heterogeneous Vehicle Routing Problem](https://ieeexplore.ieee.org/document/8541149) is an operational management problem in the field of distribution and logistics. In this problem, routes have to be designed starting from a depot to the geographically spread customer zones with an objective to minimize distance or cost and fulfilling the customer demands.
The Vehicle Routing Problem is well know in computer science and logistics industry. The decision version of VRP is NP-Complete. \
Classical algorithms do exit to solve such kinds of problems but owing to the large time frame to work out a solution, they are infeasible for larger problem instances. \
This project was essentially to develop the software implementation of [the paper](https://arxiv.org/pdf/2110.06799.pdf) on HVRP which is a variant of a general Vehicle Routing Problem. The referenced paper describes an appropriate Hamiltonian for finding a solution.

# Tutorials
Under the `Examples` section, I've been documenting the progress I've made while learning DWave.
I have had some experience working with DWave's Annealers and HybridSolvers, this time I decided to document my progress.
The examples included are of varying difficulty as well use both `BQM()` and `CQM()` and hence should be suitable for anyone trying to learn DWave's Ocean sdk. \
Moreover, [Leap platform](https://cloud.dwavesys.com/leap/examples) has very nice tutorials as well

# Screening Task
For the screening task for this cohort, I chose to work on Task #2
- Given four positive integers A, B, C, D, determine if there’s a rectangle such that the lengths of its sides are A, B, C and D (in any order).  
If any such rectangle exist return 1 else return 0.































