"""
Algorithm 3
Pseudocode:
Function: find_meeting_slots(busy_schedules, working_periods, duration)
Input:
    busy_schedules: 2D array of busy times for each person
    working_periods: List of earliest and latest available times for each person
    duration: Minimum meeting duration in minutes
Output:
    List of available meeting slots in HH:MM format

Set earliest_start = latest available start time from working_periods
Set latest_end = earliest available end time from working_periods
Combine and sort all busy schedules into combined_busy

Find free slots:
    Initialize last_end = earliest_start
    For each interval in combined_busy:
        If there's enough gap between last_end and interval start, save it as a free slot
        Update last_end to the max of last_end and interval end

Check for a final free slot between last_end and latest_end

Return the free slots in HH:MM format
"""


def convert_time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def convert_minutes_to_time(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

def find_free_intervals(busy_intervals, daily_bounds):
    earliest, latest = daily_bounds
    busy_intervals = [[earliest, earliest]] + busy_intervals + [[latest, latest]]
    busy_intervals = merge_intervals(busy_intervals)
    free_intervals = []
    for i in range(1, len(busy_intervals)):
        start_free = busy_intervals[i - 1][1]
        end_free = busy_intervals[i][0]
        if start_free < end_free:
            free_intervals.append([start_free, end_free])
    return free_intervals

def intersect_intervals(intervals_a, intervals_b):
    i, j = 0, 0
    intersection = []
    while i < len(intervals_a) and j < len(intervals_b):
        start = max(intervals_a[i][0], intervals_b[j][0])
        end = min(intervals_a[i][1], intervals_b[j][1])
        if start < end:
            intersection.append([start, end])
        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1
    return intersection

def find_common_available_times(schedules, daily_active_periods, meeting_duration):
    free_times_list = []
    for schedule, daily_bounds in zip(schedules, daily_active_periods):
        busy_intervals = [[convert_time_to_minutes(s), convert_time_to_minutes(e)] for s, e in schedule]
        daily_bounds = [convert_time_to_minutes(daily_bounds[0]), convert_time_to_minutes(daily_bounds[1])]
        free_intervals = find_free_intervals(busy_intervals, daily_bounds)
        free_times_list.append(free_intervals)
    common_available_times = free_times_list[0]
    for i in range(1, len(free_times_list)):
        common_available_times = intersect_intervals(common_available_times, free_times_list[i])
    meeting_duration_minutes = meeting_duration
    result = []
    for start, end in common_available_times:
        if end - start >= meeting_duration_minutes:
            result.append([convert_minutes_to_time(start), convert_minutes_to_time(end)])
    return result

"""" 
Sample Input
person1_schedule = [['7:00', '8:30'], ['12:00', '13:00'], ['16:00', '18:00']]
person1_daily_act = ['9:00', '19:00']
person2_schedule = [['9:00', '10:30'], ['12:20', '13:30'], ['14:00', '15:00'], ['16:00', '17:00']]
person2_daily_act = ['9:00', '18:30']
meeting_duration = 30

Function Call
schedules = [person1_schedule, person2_schedule]
daily_active_periods = [person1_daily_act, person2_daily_act]
available_times = find_common_available_times(schedules, daily_active_periods, meeting_duration)

print(available_times)


Time Complexity: For each of the N persons, their M busy intervals are sorted.
Sorting each list of intervals takes O(MlogM) time. Therefore, the time complexity is O(N*MlogM).
"""