import stripe


def createPaymentIntent(amount, email, cid, oid, mid, save_method, currency="inr"):
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            receipt_email=email,
            customer=cid,
            metadata={"order_id": oid},
        )

        if mid:
            stripe.PaymentIntent.modify(intent.id, metadata={"payment_method": mid})

        if save_method == True:
            stripe.PaymentIntent.modify(
                intent.id, metadata={"setup_future_usage": "off_session"}
            )

    except Exception as e:
        return str(e)

    return intent.clinet_secret


def createCustomer(email, name):
    customer = stripe.Customer.list(email=email)
    try:
        if customer:
            return customer
        else:
            customer = stripe.Customer.create(name=name, email=email)
            return customer
    except Exception as e:
        return str(e)


def createRefund(payid, ammount, oid, uid):
    stripe.Refund.create(
        payment_inten=payid,
        amount=ammount,
        reason="requested_by_customer",
        refund_application_fee=True,
        metadata={"order_id": oid, "user_id": uid},
    )
