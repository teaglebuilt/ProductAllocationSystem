from models import Batch, OrderLine
from datetime import date


def make_batch_and_line(sku, batch_qty, line_qty):
    return(
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )

def test_allocating_to_batch_reduces_availability():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine('order-ref', "SMALL-TABLE", 2)
    batch.allocate(line)
    assert batch.available_quantity == 18


def test_allocate_if_greater_than_required():
    small_batch, large_line = make_batch_and_line("LAMP", 2, 20)
    assert small_batch.can_allocate(large_line) is False

def test_allocate_if_smaller():
    large_batch, small_line = make_batch_and_line("Light Bulb", 20, 2)
    assert large_batch.can_allocate(small_line) is True

def test_matching_in_allocation():
    batch = Batch('Batch-03', 'Nails', qty=50,  eta=date.today())
    line = OrderLine('R-32', 'Wood', qty=3)
    batch.can_allocate(line) is False

    