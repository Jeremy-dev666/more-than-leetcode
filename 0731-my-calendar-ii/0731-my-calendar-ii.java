class MyCalendarTwo {
    private final TreeMap<Integer, Integer> timeline = new TreeMap<>();
    public MyCalendarTwo() {
        
    }
    
    public boolean book(int startTime, int endTime) {
        timeline.merge(startTime, 1, Integer::sum);
        timeline.merge(endTime, -1, Integer::sum);
        int exist = 0;
        for (int d : timeline.values()) {
            exist += d;
            if (exist > 2) {
                timeline.merge(startTime, -1, Integer::sum);
                timeline.merge(endTime, 1, Integer::sum);
                return false;
            }
        }
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(startTime,endTime);
 */