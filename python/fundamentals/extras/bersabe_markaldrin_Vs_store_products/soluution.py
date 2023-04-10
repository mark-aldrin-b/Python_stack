from module.product import product

aldrin = product("HungerDog", 20, "treats")
aldrin.update_price(.5,False).print_info()

from module.store import store
bolt = store()

bolt.add_product("Vitality", 30)

bolt.inflation(.5, 0)

bolt.set_clearance(0, .2)

bolt.sell_product(0)