import System.IO (readFile)
import Data.List (lines)
import Data.List (intercalate)

toFloats :: [[Char]] -> [Float]
toFloats xs = map fromIntegral [read x | x <- xs]

toInts :: [[Char]] -> [Int]
toInts xs = [read x | x <- xs]

parsep2 :: [[Int]] -> [Float]
parsep2 xs = read (intercalate "" (map show xs))

splitLines :: String -> [[String]]
splitLines xs = map tail (map (words . dropWhile (== ' ')) (lines xs))

q_eval :: Float -> Float -> Int
q_eval r d = abs ((floor y) - (floor x))
  where
    x = (r + sqrt (r^2 - 4.0*d))/ (-2)
    y = (r - sqrt (r^2 - 4.0*d))/ (-2)

evalRaces :: [[Float]] -> Int
evalRaces [[], []] = 1
evalRaces [r:rs, d:ds] = (q_eval r d) * evalRaces [rs, ds]

main :: IO()
main = do
  -- SET TO TRUE FOR PART2
  let part2 = False
  input_raw <- readFile "data"
  let input = map toFloats (splitLines input_raw)
  let p2_input = map parsep2 (map toInts (map splitLines input_raw))
  print (evalRaces input)
