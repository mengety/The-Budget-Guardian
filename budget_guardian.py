# 1. PERMANENT LIMITS (Set at the start of the session)
MARKETING_LIMIT = float(input("Set the Permanent Marketing Limit: "))
SOFTWARE_LIMIT = float(input("Set the Permanent Software Limit: "))

# 2. STORAGE & COUNTERS
# We start with an empty list and variables to track stats
expenses_history = []
success_count = 0  # Number of "Safe" entries
failure_count = 0  # Number of "Danger" entries
total_loss = 0.0   # Sum of amounts over the limit

# 3. DATA ENTRY LOOP
print("\n--- Start Entering Your Data (Goal: 10 entries) ---")

while len(expenses_history) < 10:
    current_count = len(expenses_history) + 1
    print(f"\nEntry #{current_count}")
    
    # Ask user for current data
    category = input("Enter Category (Marketing/Software): ").capitalize()
    amount = float(input(f"Enter amount for {category}: "))
    
    # Logic to compare with permanent limits
    limit_to_use = MARKETING_LIMIT if category == "Marketing" else SOFTWARE_LIMIT
    
    if amount > limit_to_use:
        print("🚨 DANGER: Over Limit!")
        status = "Failure"
        failure_count += 1
        total_loss += (amount - limit_to_use)
    else:
        print("✅ SAFE: Within Limit.")
        status = "Success"
        success_count += 1
    
    # Append the data to our history
    expenses_history.append({
        "ID": current_count,
        "Category": category,
        "Amount": amount,
        "Status": status
    })

# 4. FINAL ANALYTICS (Triggers after 10 entries)
print("\n" + "="*40)
print("📊 FINAL AUDIT REPORT")
print("="*40)

# Table Header
print(f"{'ID':<5} | {'Category':<12} | {'Amount':<10} | {'Status':<10}")
print("-" * 45)

# Table Rows (Looping through our stored list)
for item in expenses_history:
    print(f"{item['ID']:<5} | {item['Category']:<12} | ${item['Amount']:<9.2f} | {item['Status']:<10}")

# 5. MATHEMATICAL CALCULATIONS
success_rate = (success_count / 10) * 100
failure_rate = (failure_count / 10) * 100
avg_loss = total_loss / failure_count if failure_count > 0 else 0

print("-" * 45)
print(f"✅ Total Successes: {success_count}")
print(f"❌ Total Failures:  {failure_count}")
print(f"📈 Success Rate:    {success_rate}%")
print(f"📉 Failure Rate:    {failure_rate}%")
print(f"💸 Average Loss:    ${avg_loss:.2f}")
print("="*40)
