class MyCalendarThree {
    private final TreeMap<Integer, Integer> timeline = new TreeMap<>();
    public MyCalendarThree() {
        
    }
    
    public int book(int startTime, int endTime) {
        timeline.merge(startTime, 1, Integer::sum);
        timeline.merge(endTime, -1, Integer::sum);

        int count = 0;
        int ans = 0;
        for (int d : timeline.values()) {
            count += d;
            ans = Math.max(ans, count);
        }
        return ans;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(startTime,endTime);
 */