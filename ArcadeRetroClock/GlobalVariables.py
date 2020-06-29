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
replicationrate   = 200
VirusTopSpeed     = 1
VirusBottomSpeed  = 10
MinBright         = 100
MaxBright         = 255

OriginalMutationRate      = 500
OriginalReplicationRate   = 200
FreakoutReplicationRate   = 10   #new replication rate when a virus freaksout
MaxVirusMoves             = 100000 #after this many moves the level is over
FreakoutMoves             = 58000 #after this many moves, the viruses will replicate and mutate at a much greater rate
OriginalMutationDeathRate = 20
mutationrate      = 0
mutationdeathrate = 0
VirusMoves        = 0
ClumpingSpeed     = 10    #This modifies the speed of viruses that contact each other
ReplicationSpeed  = 1     #When a virus replicates, it will be a bit slower.  This number is added to current speed.
ChanceOfSpeedup   = 1     #determines how often a lone virus will spontaneously speed up
SlowTurnMinMoves  = 5     #number of moves a mutated virus moves before turning
SlowTurnMaxMoves  = 25    #number of moves a mutated virus moves before turning
VirusStartSpeed   = 20    #staring speed of the viruses
MaxReplications   = 5     #Maximum number of replications, if surpassed the virus dies
MaxMutations      = 5     #Maximum number of mutations, if surpassed the virus dies
InfectionChance   = 5     #Chance of one virus infecting another, lower the number greater the chance


#----------------------------
#-- PacDot                 --
#----------------------------

PacDotScore = 0
PacDotHighScore = 0



DotMatrix = [[0 for x in range(HatHeight)] for y in range(HatWidth)] 



#----------------------------
#-- DotZerk                --
#----------------------------

