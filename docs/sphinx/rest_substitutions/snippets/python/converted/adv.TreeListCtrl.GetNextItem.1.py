
                item = tree.GetFirstItem()

                while item:
                    ok = item.IsOk()
                    item = tree.GetNextItem(item)
                
                    # Do something with every tree item ...
                
