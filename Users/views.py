from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TransactionPrediction
from .predict_pipeline import predict_custom
from django.db.models import Count

# Create your views here.
def userhome(request):
    user = request.user
    return render(request, 'User/userhome.html', {'user':user})

@login_required
def prediction(request):
    result = None
    if request.method == "POST":
        # Collect input manually
        sample_input = {
            "From Bank": int(request.POST.get("from_bank")),
            "To Bank": int(request.POST.get("to_bank")),
            "Amount Received": float(request.POST.get("amount_received")),
            "Receiving Currency": request.POST.get("receiving_currency"),
            "Amount Paid": float(request.POST.get("amount_paid")),
            "Payment Currency": request.POST.get("payment_currency"),
            "Payment Format": request.POST.get("payment_format"),
        }

        # Run prediction
        result = predict_custom(sample_input)

        # Save to DB
        TransactionPrediction.objects.create(
            user=request.user,
            from_bank=sample_input["From Bank"],
            to_bank=sample_input["To Bank"],
            amount_received=sample_input["Amount Received"],
            receiving_currency=sample_input["Receiving Currency"],
            amount_paid=sample_input["Amount Paid"],
            payment_currency=sample_input["Payment Currency"],
            payment_format=sample_input["Payment Format"],
            probability=result["probability"],
            prediction=result["prediction"],
            label=result["label"],
        )

    return render(request, "User/prediction.html", {"result": result})

def datavisulization(request):
    return render(request, 'User/datavisulization.html')

def exsisting(request):
    return render(request, 'User/exsisting.html')

def proposed(request):
    return render(request, 'User/proposed.html')

@login_required
def history(request):
    user_predictions = TransactionPrediction.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "User/history.html", {"predictions": user_predictions})

@login_required
def analytics(request):
    # Total predictions by label
    prediction_counts = TransactionPrediction.objects.filter(user=request.user) \
        .values("label") \
        .annotate(count=Count("id"))

    labels = [p["label"] for p in prediction_counts]
    counts = [p["count"] for p in prediction_counts]

    # Line chart data: predictions over time (grouped by date)
    timeline_data = (
        TransactionPrediction.objects.filter(user=request.user)
        .extra(select={"day": "date(created_at)"})
        .values("day")
        .annotate(count=Count("id"))
        .order_by("day")
    )
    timeline_labels = [str(t["day"]) for t in timeline_data]
    timeline_counts = [t["count"] for t in timeline_data]

    context = {
        "labels": labels,
        "counts": counts,
        "timeline_labels": timeline_labels,
        "timeline_counts": timeline_counts,
    }
    return render(request, "User/analytics.html", context)