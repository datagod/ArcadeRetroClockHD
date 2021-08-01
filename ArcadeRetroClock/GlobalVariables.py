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
#   Version: 1.1                                                             --
#   Date:    August 1, 2021                                                  --
#   Reason:  minor fixes                                                     --
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
VirusBottomSpeed  = 20
VirusStartSpeed   = 8  #starting speed of the viruses
MinBright         = 50
MaxBright         = 255

OriginalMutationRate      = 10000
OriginalMutationDeathRate = 500
MaxMutations              = 5      #Maximum number of mutations, if surpassed the virus dies
MutationTypes             = 10     #Number of different types of mutations
OriginalReplicationRate   = 5000
replicationrate           = OriginalReplicationRate
FreakoutReplicationRate   = 10     #new replication rate when a virus freaksout
MaxVirusMoves             = 100000 #after this many moves the level is over
FreakoutMoves             = 25000  #after this many moves, the viruses will replicate and mutate at a much greater rate
VirusMoves                = 0      #used to count how many times the viruses have moved
ClumpingSpeed             = 10     #This modifies the speed of viruses that contact each other
ReplicationSpeed          = 5      #When a virus replicates, it will be a bit slower.  This number is added to current speed.
ChanceOfSpeedup           = 10     #determines how often a lone virus will spontaneously speed up
SlowTurnMinMoves          = 2      #number of moves a mutated virus moves before turning
SlowTurnMaxMoves          = 40     #number of moves a mutated virus moves before turning
MaxReplications           = 5      #Maximum number of replications, if surpassed the virus dies
InfectionChance           = 20     #Chance of one virus infecting another, lower the number greater the chance
DominanceMaxCount         = 5000   #how many ticks with there being only one virus, when reached level over
VirusNameSpeedupCount     = 500    #when this many virus strains are on the board, speed them up
ChanceOfDying             = 1000   #random chance of a virus dying
GreatChanceOfDying        = 300    #random chance of a virus dying when too many straings are alive
ChanceOfHeadingToHV       = 50000  #random chance of all viruses being interested in the same location
ChanceOfHeadingToFood     = 50     #random chance of a virus heading towards the nearest food
FoodCheckRadius           = 5      #radius around the virus when looking for food
ChanceOfTurningIntoFood   = 5      #Random chance of a dying mutating virus to turn into food
ChanceOfTurningIntoWall   = 5      #Random chance of a dying mutating virus to turn into food
VirusFoodWallLives        = 5      #Lives of food before it gets eaten and disappears
AuditSpeed                = 100    #Every X tick, an audit text window is displayed for debugging purposes
EatingSpeedAdjustment     = -10    #When a virus eats, it gets full and slows down             
SpeedIncrements           = 50     #how many chunks the speed range is cut up into, for increasing gradually
FoodBrightnessSteps       = 5      #each time a food loses life, it gets brighter by this many units
ChanceToStopEating        = 100    #chance that a virus decides to stop eating and carry on with life
ChanceOfRandomFood        = 10000  #chance that random food will show up, which will draw the viruses to it
MapOffset                 = 20     #how many pixels from the left screen does the map really start (so we don't overwrite clocks and other things)
BigFoodLives              = 1000   #lives for the big food particle
BigFoodRGB                = (255,0,0)
MaxRandomViruses          = 5      #maximum number of random viruses to place on big food maps
VirusMaxCount             = 1000   #maximum number of unique virus strains allowed


#----------------------------
#-- PacDot                 --
#----------------------------

PacDotScore = 0
PacDotHighScore = 0



DotMatrix = [[0 for x in range(HatHeight)] for y in range(HatWidth)] 



#----------------------------
#-- DotZerk                --
#----------------------------
