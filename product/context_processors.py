from .views import _cart_id
from .models import Cart, CartItem, Category

def categories(request):
    categories = Category.objects.order_by('-name')
    return dict(categories=categories)

def counter(request):
    counter_val = 0
    total = 0
    cart_items = []
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request)).first()
            if cart:
                cart_items = CartItem.objects.filter(cart=cart, active=True)
                for cart_item in cart_items:
                    total += (cart_item.product.price * cart_item.quantity)
                    counter_val += cart_item.quantity
        except Exception:
            pass
    return {
        'counter': counter_val,
        'cart_items': cart_items,
        'total': total
    }

                    
