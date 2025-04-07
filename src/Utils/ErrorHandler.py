# utils.py

import stripe


def StripeErrors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except stripe.error.CardError as e:
            return {
                "error": {
                    "status": e.http_status,
                    "code": e.code,
                    "param": e.param,
                    "message": e.user_message,
                }
            }, e.http_status

        except stripe.error.RateLimitError as e:
            return {
                "error": "Too many requests made to the API too quickly",
                "actual_error": e,
            }, 429

        except stripe.error.InvalidRequestError as e:
            return {
                "error": "Invalid parameters were supplied to Stripe's API",
                "actual_error": e,
            }, 400

        except stripe.error.AuthenticationError as e:
            return {
                "error": "Authentication with Stripe's API failed",
                "actual_error": e,
            }, 401

        except stripe.error.APIConnectionError as e:
            return {
                "error": "Network communication with Stripe failed",
                "actual_error": e,
            }, 500

        except stripe.error.StripeError as e:
            return {
                "error": "A generic error occurred with Stripe",
                "actual_error": e,
            }, 400

        except stripe.error.IdempotencyError as e:
            return {"error": "Idempotency error occurred", "actual_error": e}, 409

        except stripe.error.NotFoundError as e:
            return {"error": "Requested resource not found", "actual_error": e}, 404

        except stripe.error.ForbiddenError as e:
            return {
                "error": "API key doesn’t have permissions to perform the request",
                "actual_error": e,
            }, 403

        except stripe.error.BadRequestError as e:
            return {
                "error": "The request was unacceptable, often due to missing a required parameter",
                "actual_error": e,
            }, 400

        except stripe.error.RequestFailedError as e:
            return {
                "error": "The parameters were valid but the request failed",
                "actual_error": e,
            }, 402

        except stripe.error.ServerError as e:
            return {
                "error": "Something went wrong on Stripe’s end",
                "actual_error": e,
            }, 500

        except stripe.error.APIError as e:
            return {"error": "API error occurred", "actual_error": e}, 500

        except Exception as e:
            return {
                "error": "Something else happened, unrelated to Stripe",
                "actual_error": e,
            }, 500

    return wrapper
