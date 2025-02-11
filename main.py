import argparse

def calculate_availability(planned_production_time, downtime):
    """
    Calculate availability:
    
      availability = (planned_production_time - downtime) / planned_production_time
      
    Parameters:
      planned_production_time : Total planned production time (e.g., hours)
      downtime                : Downtime during production (e.g., hours)
      
    Returns:
      Availability as a ratio (float, where 1.0 = 100%).
    """
    if planned_production_time == 0:
        return 0
    return (planned_production_time - downtime) / planned_production_time

def calculate_performance(qty_good, scrap, cycle_rate, uptime):
    """
    Calculate performance using the following formulas:
    
      total_parts = qty_good + scrap
      ideal_parts = uptime * cycle_rate
      performance = total_parts / ideal_parts
      
    Parameters:
      qty_good  : Number of good quality units produced.
      scrap     : Number of scrap units produced.
      cycle_rate: Ideal production rate (units per hour).
      uptime    : Uptime in hours.
      
    Returns:
      Performance as a ratio (float, where 1.0 = 100%).
    """
    total_parts = qty_good + scrap
    ideal_parts = uptime * cycle_rate
    if ideal_parts == 0:
        return 0
    return total_parts / ideal_parts

def calculate_quality(qty_good, scrap):
    """
    Calculate quality:
    
      quality = qty_good / (qty_good + scrap)
      
    Parameters:
      qty_good : Number of good quality units produced.
      scrap    : Number of scrap units produced.
      
    Returns:
      Quality as a ratio (float, where 1.0 = 100%).
    """
    total = qty_good + scrap
    if total == 0:
        return 0
    return qty_good / total

def calculate_oee(availability, performance, quality):
    """
    Calculate OEE (Overall Equipment Effectiveness) as:
    
      OEE = availability * performance * quality
      
    Parameters:
      availability : Availability as a ratio.
      performance  : Performance as a ratio.
      quality      : Quality as a ratio.
      
    Returns:
      OEE as a ratio (float, where 1.0 = 100%).
    """
    return availability * performance * quality

def main():
    parser = argparse.ArgumentParser(
        description="Calculate Availability, Performance, Quality, or OEE (A x P x Q) based on production data."
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--availability", action="store_true",
                       help="Calculate Availability")
    group.add_argument("-p", "--performance", action="store_true",
                       help="Calculate Performance")
    group.add_argument("-q", "--quality", action="store_true",
                       help="Calculate Quality")
    group.add_argument("-o", "--oee", action="store_true",
                       help="Calculate OEE from Availability, Performance, and Quality percentages (A x P x Q)")
    
    args = parser.parse_args()
    
    if args.availability:
        print("Calculating Availability:")
        planned_production_time = float(input("Enter planned production time (e.g., hours): "))
        downtime = float(input("Enter downtime (e.g., hours): "))
        availability = calculate_availability(planned_production_time, downtime)
        print(f"Availability: {availability:.2%}")
    
    elif args.performance:
        print("Calculating Performance:")
        qty_good = float(input("Enter number of good quality units produced: "))
        scrap = float(input("Enter number of scrap units produced: "))
        cycle_rate = float(input("Enter ideal production rate (units per hour): "))
        uptime = float(input("Enter uptime (hours): "))
        performance = calculate_performance(qty_good, scrap, cycle_rate, uptime)
        print(f"Performance: {performance:.2%}")
    
    elif args.quality:
        print("Calculating Quality:")
        qty_good = float(input("Enter number of good quality units produced: "))
        scrap = float(input("Enter number of scrap units produced: "))
        quality = calculate_quality(qty_good, scrap)
        print(f"Quality: {quality:.2%}")
    
    elif args.oee:
        print("Calculating OEE:")
        availability = float(input("Enter Availability (as a decimal, e.g., 0.9 for 90%): "))
        performance = float(input("Enter Performance (as a decimal, e.g., 0.8 for 80%): "))
        quality = float(input("Enter Quality (as a decimal, e.g., 0.95 for 95%): "))
        oee = calculate_oee(availability, performance, quality)
        print(f"OEE: {oee:.2%}")

if __name__ == "__main__":
    main()
