
import re
from textblob import TextBlob
from transformers import pipeline

spam_keywords= [
        '100%',
        '#1',
        '$$$',
        '100% free',
        '100% Satisfied',
        '4U',
        '50% off',
        'Accept credit cards',
        'Acceptance',
        'Access',
        'Accordingly',
        'Act Now',
        'Action',
        'Ad',
        'Additional income',
        'Addresses on CD',
        'Affordable',
        'All natural',
        'All new',
        'Amazed',
        'Amazing',
        'Amazing stuff',
        'Apply now',
        'Apply Online',
        'As seen on',
        'Auto email removal',
        'Avoid',
        'Avoid bankruptcy',
        'Bargain',
        'Be amazed',
        'Be your own boss',
        'Being a member',
        'Beneficiary',
        'Best price',
        'Beverage',
        'Big bucks',
        'Bill 1618',
        'Billing',
        'Billing address',
        'Billion',
        'Billion dollars',
        'Bonus',
        'Boss',
        'Brand new pager',
        'Bulk email',
        'Buy',
        'Buy direct',
        'Buying judgments',
        'Cable converter',
        'Call',
        'Call free',
        'Call now',
        'Calling creditors',
        'Can’t live without',
        'Cancel',
        'Cancel at any time',
        'Cannot be combined with any other offer',
        'Cards accepted',
        'Cash',
        'Cash bonus',
        'Cashcashcash',
        'Casino',
        'Celebrity',
        'Cell phone cancer scam',
        'Cents on the dollar',
        'CertifiedChance',
        'Cheap',
        'Check',
        'Check or money order',
        'Claims',
        'Claims not to be selling anything',
        'Claims to be in accordance with some spam law',
        'Claims to be legal',
        'Clearance',
        'Click',
        'Click below',
        'Click here',
        'Click to remove',
        'Collect',
        'Collect child support',
        'Compare',
        'Compare rates',
        'Compete for your business',
        'Confidentially on all orders',
        'Congratulations',
        'Consolidate debt and credit',
        'Consolidate your debt',
        'Copy accurately',
        'Copy DVD',
        'Costs',
        'Credit',
        'Credit bureaus',
        'Credit card offers',
        'Cures',
        'Cures baldness',
        'Deal',
        'Dear',
        'Debt',
        'Diagnostics',
        'Dig up dirt on friends',
        'Direct email',
        'Direct marketing',
        'Discount',
        'Do it today',
        'Don’t delete',
        'Don’t hesitate',
        'Dormant',
        'Double your',
        'Double your cash',
        'Double your income',
        'Drastically reduced',
        'Earn',
        'Earn extra cash',
        '$Earn extra cash',
        'Earn per week',
        'Easy terms',
        'Eliminate bad credit',
        'Eliminate debt',
        'Email harvest',
        'Email marketing',
        'Exclusive deal',
        'Expect to earn',
        'Expire',
        'Explode your business',
        'Extra',
        'Extra cash',
        'Extra income',
        'F r e e',
        'Fantastic',
        'Fantastic deal',
        'Fast cash',
        'Fast',
        'Viagra',
        'Viagra delivery',
        'Financial freedom',
        'Financially independent',
        'For free',
        'For instant access',
        'For just $',
        'For Only',
        'For you',
        'Form',
        'Free',
        'Free access',
        'Free cell phone',
        'Free consultation',
        'Free DVD',
        'Free gift',
        'Free grant money',
        'Free hosting',
        'Free info',
        'Free installation',
        'Free Instant',
        'Free investment',
        'Free leads',
        'Free membership',
        'Free money',
        'Free offer',
        'Free preview',
        'Free priority mail',
        'Free quote',
        'Free sample',
        'Free trial',
        'Free website',
        'Freedom',
        'Friend',
        'Full refund',
        'Get',
        'Get it now',
        'Get out of debt',
        'Get paid',
        'Get started now',
        'Gift certificate',
        'Give it away',
        'Giving away',
        'Great',
        'Great offer',
        'Guarantee',
        'Guaranteed',
        'Have you been turned down?',
        'Hello',
        'Here',
        'Hidden',
        'Hidden assets',
        'Hidden charges',
        'Home',
        'Home based',
        'Home employment',
        'Home based business',
        'Human growth hormone',
        'If only it were that easy',
        'Important information regarding',
        'In accordance with laws',
        'Income',
        'Income from home',
        'Increase sales',
        'Increase traffic',
        'Increase your sales',
        'Incredible deal',
        'Info you requested',
        'Information you requested',
        'Instant',
        'Insurance',
        'Insurance',
        'Internet market',
        'Internet marketing',
        'Investment',
        'Investment decision',
        'It’s effective',
        'Join millions',
        'Join millions of Americans',
        'Junk',
        'Laser printer',
        'Leave',
        'Legal',
        'Life',
        'Life Insurance',
        'Lifetime',
        'Limited',
        'limited time',
        'Limited time offer',
        'Limited time only',
        'Loan',
        'Long distance phone offer',
        'Lose',
        'Lose weight',
        'Lose weight spam',
        'Lower interest rates',
        'Lower monthly payment',
        'Lower your mortgage rate',
        'Lowest insurance rates',
        'Lowest Price',
        'Luxury',
        'Luxury car',
        'Mail in order form',
        'Maintained',
        'Make $',
        'Make money',
        'Marketing',
        'Marketing solutions',
        'Mass email',
        'Medicine',
        'Medium',
        'Meet singles',
        'Member',
        'Member stuff',
        'Message contains',
        'Message contains disclaimer',
        'Million',
        'Million dollars',
        'Miracle',
        'MLM',
        'Money',
        'Money back',
        'Money making',
        'Month trial offer',
        'More Internet Traffic',
        'Mortgage',
        'Mortgage rates',
        'Multi-level marketing',
        'Name brand',
        'Never',
        'New customers only',
        'New domain extensions',
        'Nigerian',
        'No age restrictions',
        'No catch',
        'No claim forms',
        'No cost',
        'No credit check',
        'No disappointment',
        'No experience',
        'No fees',
        'No gimmick',
        'No hidden',
        'No hidden Costs',
        'No interests',
        'No inventory',
        'No investment',
        'No medical exams',
        'No middleman',
        'No obligation',
        'No purchase necessary',
        'No questions asked',
        'No selling',
        'No strings attached',
        'No-obligation',
        'Not intendedNot junk',
        'Not spam',
        'Now',
        'Now only',
        'Obligation',
        'Offshore',
        'Offer',
        'Offer expires',
        'Once in lifetime',
        'One hundred percent free',
        'One hundred percent guaranteed',
        'One time',
        'One time mailing',
        'Online biz opportunity',
        'Online degree',
        'Online marketing',
        'Online pharmacy',
        'Only',
        'Only $',
        'Open',
        'Opportunity',
        'Opt in',
        'Order',
        'Order now',
        'Order shipped by',
        'Order status',
        'Order today',
        'Outstanding values',
        'Passwords',
        'Pennies a day',
        'Per day',
        'Per week',
        'Performance',
        'Phone',
        'Please read',
        'Potential earnings',
        'Pre-approved',
        'Presently',
        'Price',
        'Print form signature',
        'Print out and fax',
        'Priority mail',
        'Prize',
        'Problem',
        'Produced and sent out',
        'Profits',
        'Promise',
        'Promise you',
        'Purchase',
        'Pure Profits',
        'Quote',
        'Rates',
        'Real thing',
        'Refinance',
        'Refinance home',
        'Refund',
        'Removal',
        'Removal instructions',
        'Remove',
        'Removes wrinkles',
        'Request',
        'Requires initial investment',
        'Reserves the right',
        'Reverses',
        'Reverses aging',
        'Risk free',
        'Rolex',
        'Round the world',
        'S 1618',
        'Safeguard notice',
        'Sale',
        'Sample',
        'Satisfaction',
        'Satisfaction guaranteed',
        'Save $',
        'Save big money',
        'Save up to',
        'Score',
        'Score with babes',
        'Search engine listings',
        'Search engines',
        'Section 301',
        'See for yourself',
        'Sent in compliance',
        'Serious',
        'Serious cash',
        'Serious only',
        'Shopper',
        'Shopping spree',
        'Sign up free today',
        'Social security number',
        'Solution',
        'Spam',
        'Special promotion',
        'Stainless steel',
        'Stock alert',
        'Stock disclaimer statement',
        'Stock pick',
        'Stop',
        'Stop snoring',
        'Strong buy',
        'Stuff on sale',
        'Subject to cash',
        'Subject to credit',
        'Subscribe',
        'Success',
        'Supplies',
        'Supplies are limited',
        'Take action',
        'Take action now',
        'Talks about hidden charges',
        'Talks about prizes',
        'Teen',
        'Tells you it’s an ad',
        'Terms',
        'Terms and conditions',
        'The best rates',
        'The following form',
        'They keep your money',
        'no refund!',
        'no refund',
        'They’re just giving it away',
        'This isn’t a scam',
        'This isn’t junk',
        'This isn’t spam',
        'This won’t last',
        'Thousands',
        'Time limited',
        'Traffic',
        'Trial',
        'Undisclosed recipient',
        'University diplomas',
        'Unlimited',
        'Unsecured credit',
        'Unsecured debt',
        'Unsolicited',
        'Unsubscribe',
        'Urgent',
        'US dollars',
        'Vacation',
        'Vacation offers',
        'Valium',
        'Vicodin',
        'Visit our website',
        'Wants credit card',
        'Warranty',
        'We hate spam',
        'We honor all',
        'Web traffic',
        'Weekend getaway',
        'Weight',
        'Weight loss',
        'What are you waiting for?',
        'What’s keeping you?',
        'While supplies last',
        'While you sleep',
        'Who really wins?',
        'Why pay more?',
        'Wife',
        'Will not believe your eyes',
        'Win',
        'Winner',
        'Winning',
        'Won',
        'Work from home',
        'Xanax',
        'You are a winner!',
        'You have been selected',
        'Your income',
        'Orders shipped by',
        'Additional',
        'Compete for your business',
        'Earn $',
        'Homebased business',
        'Work at home',
        'Big bucks Cash',
        'CheckClaims',
        'Cost',
        'Credit bureaus Discount',
        'Easy terms F r e e',
        'Loans',
        'Pennies a day Price',
        'Pure profit',
        'Save',
        '$Save',
        '$Save big money',
        'Accept Credit Cards',
        'Costs',
        'Avoid bankruptcy',
        'Lower interest rate',
        'Acceptance',
        'Chance',
        'Dear',
        'Multi level marketing',
        'Notspam',
        'Sales',
        'SubscribeThe following form',
        'This isn\'t junk',
        'This isn\'t spam',
        'Cures baldness',
        'Fast Viagra delivery',
        'Lose weightLose weight spam',
        '#1',
        'Satisfied',
        'Join millions of',
        'Americans',
        'Being a member',
        'Not intended',
        'Off shore',
        'Prizes',
        'You’re a Winner!',
        'Free',
        'All natural',
        'Certified',
        'Access',
        'Act Now!',
        'Can\'t live without',
        'Don\'t delete',
        'Don\'t hesitate',
        'Addresses on CD',
        'Copy DVDs'
    ] # type: ignore

profane_words = "" ... add list of bad or inappropriate words here
"
"""
profane_words = profane_words.split()
# Load pre-trained model for toxicity detection
toxic_model = pipeline("text-classification", model="unitary/toxic-bert")

# List of offensive words for profanity detection (extend this list)


# List of spammy keywords (extend this list)


# Preprocess the input text (normalize and clean up)
def preprocess_text(text):
    # Remove URLs, emails, or any special characters
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuation and special characters
    
    # Convert to lowercase
    text = text.lower().strip()
    
    return text

# Check for profanity by matching words from a list
def check_profanity(text):
    found_profanity = [word for word in profane_words if word in text]
    return found_profanity

# Detect toxicity using a pre-trained model
def detect_toxicity(text):
    result = toxic_model(text)
    return result[0]['label']

# Check for spam by looking for known keywords
def check_spam(text):
    found_spam = [keyword for keyword in spam_keywords if keyword in text]
    return found_spam

# Analyze sentiment (optional, negative sentiment might indicate toxicity)
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Range from -1 (negative) to 1 (positive)
    return sentiment

# Main moderation function to check the content
def moderate_content(text):
    # Preprocess the text
    text_clean = preprocess_text(text)
    
    # Check for profanity
    profanity = check_profanity(text_clean)
    
    # Check for toxicity
    toxicity = detect_toxicity(text_clean)
    
    # Check for spam
    spam = check_spam(text_clean)
    
    # Analyze sentiment (optional)
    sentiment = analyze_sentiment(text_clean)
    
    # Flag content if harmful features are detected
    flags = []
    
    if profanity:
        flags.append(f"Profanity detected: {', '.join(profanity)}")
    if toxicity == "TOXIC":
        flags.append("Toxicity detected.")
    if spam:
        flags.append(f"Spam detected: {', '.join(spam)}")
    if sentiment < -0.5:
        flags.append("Negative sentiment detected.")
    
    if not flags:
        return "Content is clean."
    else:
        return f"Content flagged: {', '.join(flags)}"

# Test the system with sample content
if __name__ == "__main__":
    # Sample harmful content
    sample_content = "U are such a shit brat"
    print(f"Sample Content: {sample_content}")
    print(moderate_content(sample_content))
    print()

    # Sample clean content
    clean_content = "This is a really interesting discussion!"
    print(f"Clean Content: {clean_content}")
    print(moderate_content(clean_content))
