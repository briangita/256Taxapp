from django.shortcuts import render

# Create your views here.
# This function handles requests to the homepage
def homePage(request):

    # Default values (used when page first loads)
    income = 0
    total_paye = 0
    total_nssf = 0
    total_deductions = 0
    net_income = 0

    # Check if the form was submitted
    if request.method == "POST":

        # Get income from the form input
        income = request.POST.get("income")

        try:
            # Convert income to integer (for calculations)
            income = int(income)

            # -----------------------------
            # NSSF CALCULATION (10%)
            # -----------------------------
            nssf_rate = 10 / 100
            total_nssf = income * nssf_rate

            # -----------------------------
            # PAYE TAX CALCULATION (UGANDA)
            # -----------------------------
            # Apply different tax rates based on income bands

            if income <= 235000:
                # No PAYE tax for income up to 235,000
                total_paye = 0

            elif income <= 335000:
                # 10% on amount above 235,000
                total_paye = (income - 235000) * 0.10

            elif income <= 410000:
                # UGX 10,000 + 20% on amount above 335,000
                total_paye = 10000 + ((income - 335000) * 0.20)

            elif income <= 10000000:
                # UGX 25,000 + 30% on amount above 410,000
                total_paye = 25000 + ((income - 410000) * 0.30)

            else:
                # High income bracket:
                # 30% on amount above 410,000
                # + extra 10% on amount above 10,000,000
                total_paye = (
                    25000
                    + ((income - 410000) * 0.30)
                    + ((income - 10000000) * 0.10)
                )

            # -----------------------------
            # TOTAL DEDUCTIONS
            # -----------------------------
            # Combine PAYE + NSSF
            total_deductions = total_paye + total_nssf

            # -----------------------------
            # NET INCOME
            # -----------------------------
            # Final take-home salary
            net_income = income - total_deductions

        except (TypeError, ValueError):
            # If user enters invalid input (e.g. text), reset values
            income = 0
            total_paye = 0
            total_nssf = 0
            total_deductions = 0
            net_income = 0

    # -----------------------------
    # CONTEXT (DATA SENT TO HTML)
    # -----------------------------
    context = {
        "income": income,
        "total_paye": round(total_paye),
        "total_nssf": round(total_nssf),
        "total_deductions": round(total_deductions),
        "net_income": round(net_income),
    }
    # Render the HTML page and pass the calculated values
    return render(request, "home.html", context)
    return render(request, "home.html")