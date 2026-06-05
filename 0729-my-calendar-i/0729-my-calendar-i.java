class MyCalendar {
    private final TreeMap<Integer, Integer> timeline = new TreeMap<>();
    public MyCalendar() {
        
    }
    
    public boolean book(int startTime, int endTime) {
        Integer prev = timeline.floorKey(startTime);
        Integer next = timeline.ceilingKey(startTime);
        if (prev != null && timeline.get(prev) > startTime) return false;
        if (next != null && next < endTime) return false;

        timeline.put(startTime, endTime);
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(startTime,endTime);
 */