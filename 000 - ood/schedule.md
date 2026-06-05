## 调度器设计(不允许有冲突)
```java
class Schedule {
    private final TreeMap<Integer, Integer> timeline = new TreeMap<>();

    public boolean add(int start, int end) {
        Integer prev = timeline.floorKey(start);
        Integer next = timeline.ceilingKey(start);
        if (prev != null && timeline.get(prev) > start) { 
            return false;
        }
        if (next != null && next < end) { 
            return false;
        }
        timeline.put(start, end);
        return true;
    }
}
```

## 调度器设计(允许k次冲突)
- 扫描线，看在一个时间段内，是否有K个时间同时在发生
```java
class Scheduler { 
    private final TreeMap<Integer, Integer> timeline = new TreeMap<>();
    private final int k;
    public boolean book(int start, int end) { 
        // 这个时刻进来一个任务
        timeline.merge(start, 1, Integer::sum);
        // 这个时刻离开一个任务
        timeline.merge(end, -1, Integer::sum);

        int count = 0;
        int sum = 0;
        for (int d : timeline.values()) {
            count += d;
            sum = Math.max(sum, count);
            if (count > k) {
                // 回退之前的操作
                timeline.merge(start, -1, Integer::sum);
                timeline.merge(end, 1, Integer::sum);
                return false;
            }
        }
        return true;
    }
}
```
## 调度器设计(查询某个时刻有多少任务在同时执行)
```java
class Scheduler {
    private TreeMap<Integer, Integer> timeline = new TreeMap<>();

    public void addTasks(List<int[]> tasks) {
        for (int[] task : tasks) {
            timeline.merge(task[0], 1, Integer::sum);
            timeline.merge(task[1], -1, Integer::sum);
        }
    }

    public int query(int time) {
        int count = 0;
        for (Map.Entry<Integer, Integer> entry : timeline.entrySet()) {
            if (entry.getKey() > time) break;
            count += entry.getValue();
        }
        return count;
    }
}
```