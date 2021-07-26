import Foundation
struct Location{
  var index: Int
  var time: Int
}

var line = readLine()!.split(separator: " ").map{Int(String($0))!}
let n = line[0]
let k = line[1]

func bfs(_ s: Int, _ e: Int, _ time: Int){
  var queue: [Location] = [Location(index: s, time: 0)]
  var visit = Array(repeating: false, count: 100005)
  visit[s] = true
  while !queue.isEmpty{
    let location = queue.removeFirst()
    if location.index == e{
      print(location.time)
      break
    }
    if location.index * 2 <= 100000, !visit[location.index * 2]{
      queue.append(Location(index: location.index * 2, time: location.time + 1))
      visit[location.index * 2] = true
    }
    if location.index - 1 >= 0, !visit[location.index - 1]{
      queue.append(Location(index: location.index - 1, time: location.time + 1))
      visit[location.index - 1] = true
    }
    if location.index + 1 <= 100000, !visit[location.index + 1]{
      queue.append(Location(index: location.index + 1, time: location.time + 1))
      visit[location.index + 1] = true
    }
  }
}

if k == n{
  print(0)
}else if n > k{
  print(n - k)
}else{
  bfs(n,k,0)
}
