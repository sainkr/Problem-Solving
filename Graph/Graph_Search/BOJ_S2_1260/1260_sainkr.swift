import Foundation
let lineArr = readLine()!.split(separator: " ").map{Int(String($0))!}
let n = lineArr[0]
let m = lineArr[1]
let v = lineArr[2]

var graph: [Int: [Int]] = [:]
var dfsArr: [Int] = []
var bfsArr: [Int] = []

for _ in 1...m{
  let lineArr = readLine()!.split(separator: " ").map{Int(String($0))!}
  if graph[lineArr[0]] == nil{
    graph[lineArr[0]] = [lineArr[1]]
  }else {
    graph[lineArr[0]]?.append(lineArr[1])
  }
  if graph[lineArr[1]] == nil{
    graph[lineArr[1]] = [lineArr[0]]
  }else {
    graph[lineArr[1]]?.append(lineArr[0])
  }
}

func dfs(_ s: Int){
  var list: [Int] = []
  var stack = [s]
  while !stack.isEmpty{
    let node = stack.removeLast()
    if !list.contains(node){
      list.append(node)
      print(node, terminator: " ")
      if let nearNode = graph[node]{
        stack.append(contentsOf: nearNode.sorted(by: >))
      }
    }
  }
}

func bfs(_ s: Int){
  var list: [Int] = []
  var queue: [Int] = [s]
  while !queue.isEmpty{
    let node = queue.removeFirst()
    if !list.contains(node){
      list.append(node)
      print(node, terminator: " ")
      if let nearNode = graph[node]{
        queue.append(contentsOf: nearNode.sorted())
      }
    }
  }
}

dfs(v)
print()
bfs(v)
