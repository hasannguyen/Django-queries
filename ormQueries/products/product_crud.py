from .models import Product


class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model_name):
        return Product.objects.get(model=model_name)

    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, rating_name):
        return Product.objects.filter(rating=rating_name)

    @classmethod
    def by_rating_range(cls, first_rating, second_rating):
        return Product.objects.filter(rating__range=(first_rating, second_rating))

    @classmethod
    def by_rating_and_color(cls, rating_name, color_name):
        return Product.objects.filter(rating=rating_name, color=color_name)

    @classmethod
    def by_rating_or_color(cls, rating_name, color_name):
        return Product.objects.filter(rating=rating_name) | Product.objects.filter(
            color=color_name
        )

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color=None).count()

    @classmethod
    def below_price_or_above_rating(cls, first_price, second_rating):
        return Product.objects.filter(
            price_cents__lt=first_price
        ) | Product.objects.filter(rating__gt=second_rating)

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by("category", "-price_cents")
