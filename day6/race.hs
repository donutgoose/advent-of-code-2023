import System.IO (readFile)
import Data.List (intercalate)
import Data.List (singleton)

toDoubles :: [[Char]] -> [Double]
toDoubles xs = [read x :: Double | x <- xs]

parsep2 :: [Char] -> [[Double]]
parsep2 xs = [[read x :: Double | x <- (head z)],[read x :: Double | x <- (head (tail z))]]
  where
    z = map singleton (map (intercalate "") (splitLines xs))

splitLines :: String -> [[String]]
splitLines xs = map tail (map (words . dropWhile (== ' ')) (lines xs))

q_eval :: Double -> Double -> Int
q_eval r d = abs ((floor y) - (floor x))
  where
    x = (r + sqrt (r^2 - 4.0*d))/ (-2)
    y = (r - sqrt (r^2 - 4.0*d))/ (-2)

evalRaces :: [[Double]] -> Int
evalRaces [[], []] = 1
evalRaces [r:rs, d:ds] = (q_eval r d) * evalRaces [rs, ds]

main :: IO()
main = do
  input_raw <- readFile "data"
  let input = map toDoubles (splitLines input_raw)
  let p2_input = parsep2 input_raw
  print "Part 1:"
  print (evalRaces input)
  print "Part 2:"
  print (evalRaces p2_input)
