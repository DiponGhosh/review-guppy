def DecisionMake(result):
    result_text=""
    pos = float(result[0])
    neg = float(result[1])
    neu = float(result[2])

    pos_neu = 0.00
    neg_neu = 0.00

    result_logo_indicator = 0
    
    if neg == 0.00:
        pos_neu = pos + neu
    elif pos == 0.00:
        neg_neu = neg + neu
    else:
        ratio = pos / neg
        pos_neu = float( format( (pos + ( ( neu / (ratio + 1) ) * ratio )), '.2f' ) )
        neg_neu = float( format( (neg + ( ( neu / (ratio + 1) ) * 1 )), '.2f' ) )
    
    if pos == 100.00 and neg == 0.00 and neu == 0.00:
        result_text="It seems all the reviews are positive. So, definitely you should go for it."
        result_logo_indicator = 0
    
    elif pos == 0.00 and neg == 0.00 and neu == 100.00:
        result_text = "All the reviews for this product are found to be neutral. You can try it or you can go for another similar product."
        result_logo_indicator = 2
    
    elif pos == 0.00 and neg == 100.00 and neu == 0.00:
        result_text = "All the reviews for this product are found to be negative. So, we would recommend you to stay away from this product."
        result_logo_indicator = 1

    elif pos == 50.00 and neg == 0.00 and neu == 50.00:
        result_text = "As there are no negative reviews, you can go for the product."
        result_logo_indicator = 0

    elif pos == 0.00 and neg == 50.00 and neu == 50.00:
        result_text = "As there are no positive reviews, we recommend you to stay away from the product."
        result_logo_indicator = 1

    elif pos == 50.00 and neg == 50.00 and neu == 0.00:
        result_text = "As the number of positive and negative reviews are equal, you can try it. But we recommend you to go for similar product. " 
        result_logo_indicator = 2

    else:
        if pos_neu >= 90.00:
            result_text = "Reviews of the product are very good and most people expressed positive feeling about this product. You can surely go for it."
            result_logo_indicator = 0

        elif pos_neu >= 75.00 and pos_neu < 90:
            result_text = "Most reviews for the product have expressed positive feelings. Though there are some negative and neutral reviews, You Can Purchase it."
            result_logo_indicator = 0

        elif pos_neu >= 70.00 and pos_neu < 75.00:
            result_text = "Reviews of this product are heavy on positive side. So, you can purchase it."
            result_logo_indicator = 0

        elif pos_neu >= 65 and pos_neu < 70.00:
            result_text = "For this product, positive reviews are more than negative ones though, there are a good chance of being good. So, if you want this product, you can buy it."
            result_logo_indicator = 2

        elif pos_neu >= 55 and pos_neu < 65:
            result_text = "We found that positive reviews are below the standard. So, we would recommend you to go for another similar kind of product or you can buy if you only need this."
            result_logo_indicator = 2

        elif pos_neu < 55 and pos_neu >= 45:
            result_text = "We found that positive and negative reviews are almost equal. We would recommend you to go for another similar kind of product or you can buy if you only need this."
            result_logo_indicator = 2

        else:
            result_text = "Negative Reviews are higher in number than positive or neutral reviews. We would recommend you not to buy this product."  
            result_logo_indicator = 1

    
    return result_text, result_logo_indicator



#result = [73.00, 16.00, 11.00]
#print((DecisionMake(result)))