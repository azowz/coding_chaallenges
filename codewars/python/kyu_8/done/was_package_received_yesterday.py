

def was_package_received_yesterday(tz_from, tz_to, start, duration):
    time_zone_difference = tz_to - tz_from
    delivery_time_at_tz_to = start + duration + time_zone_difference

    print(f"Delivery time at recipient's timezone: {delivery_time_at_tz_to}")
    
    return delivery_time_at_tz_to < 0

print(was_package_received_yesterday(7, -3, 5, 3))  # Should return True
print(was_package_received_yesterday(0, 0, 0, 0))
print(was_package_received_yesterday(1, 1, 0, 1))  # Should return False
print(was_package_received_yesterday(7, 1, 5, 0))  # Should return False