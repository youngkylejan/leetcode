# Largest Rectangle in Histogram

**Monotonous List, Stack**

> **Maintain a monotonous ascending list**  
> When the current height will influence the ascending monotony,
> elements in ascending list should be pop up and calculate the maximal area

#

> **Elements in ascending list have specific orders**  
> The calculation between previous element and current position will cover the common area of back element,
> then the maximal area will exists in this continuous section between queue.front position and current position  

#
#
#

```
Take the case [1, 5, 6, 2, 3] as an example  
After scanning first three elements because they match ascending order  
stack = [0, 1, 2]

Then at the position 3, height is 2 which influences the ascending order in the stack  
Then pop out position 2, calculate the area between position 2 and current positin 3  
area = max(area, (3 - 1 - 1) * 6)

Keep poping the position 1, calculate the area between position 1 and current position 3  
area = max(area, (3 - 0 - 1) * 5)

Then height[3] > height[0], which does not influence ascending order  
stack = [0, 3]

After scanning, stack = [0, 3, 4]

Then scanning is over, **the current index will be 5 
Pop out position 4, calculate the area between position 4 and current index 5  
area = max(area, (5 - 3 - 1) * 3)

Pop out position 3, calculate the area between position 3 and current index 5  
area = max(area, (5 - 0 - 1) * 2)

Pop out position 0, calculate the area between position 0 and current index 5  
area = max(area, 5 * 1)
```

#

> At the last time pop, stack will be empty, which means that both of the back position's height and
> the previous position's height will be larger than the top item's.  
> **Then the width will be length of list**
