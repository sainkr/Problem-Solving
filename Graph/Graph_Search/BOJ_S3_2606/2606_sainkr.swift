import Foundation

let firstLine = readLine()!.components(separatedBy: " ").map{Int($0)!}
let n = firstLine[0]
let secondLine = readLine()!.components(separatedBy: " ").map{Int($0)!}
let v = secondLine[0]
var graph: [Int : [Int]] = [:]

for _ in 1...v{
  let line = readLine()!.components(separatedBy: " ").map{Int($0)!}
  if graph[line[0]] == nil {
    graph[line[0]] = [line[1]]
  }else {
    graph[line[0]]?.append(line[1])
  }
  if graph[line[1]] == nil {
    graph[line[1]] = [line[0]]
  }else {
    graph[line[1]]?.append(line[0])
  }
}

func dfs()-> Int{
  var visit: [Int] = []
  var stack: [Int] = [1]
  while !stack.isEmpty{
    let computer = stack.removeLast()
    if !visit.contains(computer){
      visit.append(computer)
      if let nearNode = graph[computer]{
        stack.append(contentsOf: nearNode)
      }
    }
  }
  return visit.count - 1
}

print(dfs())
