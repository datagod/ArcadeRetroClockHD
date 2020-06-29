#------------------------------------------------------------------------------
#                                                                            --
#      _    ____   ____    _    ____  _____    ____ _     ___   ____ _  __   --
#     / \  |  _ \ / ___|  / \  |  _ \| ____|  / ___| |   / _ \ / ___| |/ /   --
#    / _ \ | |_) | |     / _ \ | | | |  _|   | |   | |  | | | | |   | ' /    --
#   / ___ \|  _ <| |___ / ___ \| |_| | |___  | |___| |__| |_| | |___| . \    --
#  /_/   \_\_| \_\\____/_/   \_\____/|_____|  \____|_____\___/ \____|_|\_\   --
#                                                                            --
#                                                                            --
#  Global Variables                                                           --
#                                                                            --
#------------------------------------------------------------------------------
#   Version: 1.0                                                             --
#   Date:    June 11, 2020                                                   --
#   Reason:  Initial Creation                                                --
#------------------------------------------------------------------------------




MainSleep        = 0
FlashSleep       = 0
ScrollSleep      = 0
TinyClockStartHH = 0
TinyClockHours   = 0
CPUModifier      = 0
Gamma            = 0
HatWidth         = 16
HatHeight        = 16



PacDotHighScore = 0



#-----------------------------
# Outbreak Global Variables --
#-----------------------------
VirusTopSpeed     = 1
VirusBottomSpeed  = 5
VirusStartSpeed   = 15    #starting speed of the viruses
MinBright         = 100
MaxBright         = 255

OriginalMutationRate      = 500
OriginalReplicationRate   = 1000
replicationrate           = OriginalReplicationRate
FreakoutReplicationRate   = 10   #new replication rate when a virus freaksout
MaxVirusMoves             = 5000 #after this many moves the level is over
FreakoutMoves             = 4500 #after this many moves, the viruses will replicate and mutate at a much greater rate
OriginalMutationDeathRate = 2
mutationrate      = 0
mutationdeathrate = 5
VirusMoves        = 0
ClumpingSpeed     = 10    #This modifies the speed of viruses that contact each other
ReplicationSpeed  = 1     #When a virus replicates, it will be a bit slower.  This number is added to current speed.
ChanceOfSpeedup   = 1     #determines how often a lone virus will spontaneously speed up
SlowTurnMinMoves  = 5     #number of moves a mutated virus moves before turning
SlowTurnMaxMoves  = 25    #number of moves a mutated virus moves before turning
MaxReplications   = 2     #Maximum number of replications, if surpassed the virus dies
MaxMutations      = 5     #Maximum number of mutations, if surpassed the virus dies
InfectionChance   = 1     #Chance of one virus infecting another, lower the number greater the chance
DominanceMaxCount = 500   #how many ticks with there being only one virus, when reached level over


#----------------------------
#-- PacDot                 --
#----------------------------

PacDotScore = 0
PacDotHighScore = 0



DotMatrix = [[0 for x in range(HatHeight)] for y in range(HatWidth)] 



#----------------------------
#-- DotZerk                --
#----------------------------

