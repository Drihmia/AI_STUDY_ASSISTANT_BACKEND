import random
import string
from bs4 import BeautifulSoup

# Function to generate a random string of given length (increased to 16 characters)
def generate_random_string(length=32):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

# Function to update form with unique IDs
def update_form_with_unique_ids(form_html):
    # Parse the HTML
    soup = BeautifulSoup(form_html, 'html.parser')

    # Find all form elements
    form_elements = soup.find_all(['input', 'textarea', 'select', 'button'])

    # Assign unique random IDs to each element and update the corresponding label
    for element in form_elements:

        old_id = element.get('id')
        if not old_id:
            continue

        # Generate a unique ID for the element
        unique_id = generate_random_string()

        # Update the element with the unique ID
        element['id'] = unique_id

        # Check if there's a label associated with this element
        label = soup.find('label', {'for': old_id})
        if label:
            # If the label is found, update its 'for' attribute to match the new ID
            label['for'] = unique_id

    return str(soup)


def update_time_in_time_tag(message, time):
    # Parse the HTML
    soup = BeautifulSoup(message, 'html.parser')

    # Find all time tags
    time_tags = soup.find_all('time')

    # Update the time attribute in each time tag
    for time_tag in time_tags:
        time_tag.string = time

        # Remove the 'dir' attribute if present
        if time_tag.has_attr('dir'):
            del time_tag['dir']

        # Check if the time tag has a previous sibling and if it is not a <br> tag
        if (not time_tag.previous_sibling or time_tag.previous_sibling.name != "br"):
            br_tag = soup.new_tag("br")
            # Insert the <br> before the target tag
            time_tag.insert_before(br_tag)

    return str(soup)


if __name__ == '__main__':
    # Example form HTML
    form_html = '''
    <form id="-65d61788-8db9-4c49-af3f-4e3a54fe83eb" class="space-y-6" style="display: block;" data-gtm-form-interact-id="1">
        <div>
            <label for="question1" class="block text-sm font-medium text-gray-700">Question 1: Vrai ou Faux</label>
            <p class="mt-1 text-gray-700">Indiquez si l'affirmation suivante est vraie ou fausse: "La chimie est la seule science qui nécessite des mesures précises."</p>
            <select id="question1" name="question1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" data-gtm-form-interact-field-id="1">
                <option value="true">Vrai</option>
                <option value="false">Faux</option>
            </select>
        </div>

        <div>
            <label for="question2" class="block text-sm font-medium text-gray-700">Question 2: Choix multiple</label>
            <p class="mt-1 text-gray-700">Parmi les suivants, lequel représente le mieux un objectif de la mesure <span class="font-semibold">continue</span> en chimie?</p>
            <ul class="mt-2 space-y-2">
                <li>
                    <div class="flex items-center">
                        <input id="question2_option1" name="question2" type="radio" value="option1" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500" data-gtm-form-interact-field-id="2">
                        <label for="question2_option1" class="ml-3 block text-sm font-medium text-gray-700">Mesurer le pH d'une solution à un instant précis</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question2_option2" name="question2" type="radio" value="option2" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500" data-gtm-form-interact-field-id="3">
                        <label for="question2_option2" class="ml-3 block text-sm font-medium text-gray-700">Suivre l'évolution du pH d'une réaction au cours du temps</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question2_option3" name="question2" type="radio" value="option3" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question2_option3" class="ml-3 block text-sm font-medium text-gray-700">Déterminer la masse exacte d'un échantillon solide</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question2_option4" name="question2" type="radio" value="option4" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question2_option4" class="ml-3 block text-sm font-medium text-gray-700">Identifier la présence d'un ion spécifique dans une solution</label>
                    </div>
                </li>
            </ul>
        </div>

        <div>
            <label for="question3" class="block text-sm font-medium text-gray-700">Question 3: Remplir les blancs</label>
            <p class="mt-1 text-gray-700">La _________ massique se calcule en divisant la _________ du soluté par le _________ de la solution.</p>
            <input type="text" id="question3_1" name="question3_1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Premier blanc" data-gtm-form-interact-field-id="4">
            <input type="text" id="question3_2" name="question3_2" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Deuxième blanc" data-gtm-form-interact-field-id="5">
             <input type="text" id="question3_3" name="question3_3" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Troisième blanc" data-gtm-form-interact-field-id="6">
        </div>

        <div>
            <label for="question4" class="block text-sm font-medium text-gray-700">Question 4: Réponse courte</label>
            <p class="mt-1 text-gray-700">Pourquoi est-il parfois préférable d'utiliser une mesure approximative plutôt qu'une mesure précise en chimie?</p>
            <textarea id="question4" name="question4" rows="2" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Votre réponse" data-qb-tmp-id="lt-269641" spellcheck="false" data-gramm="false" data-gtm-form-interact-field-id="7"></textarea>
        </div>

        <div>
            <label for="question5" class="block text-sm font-medium text-gray-700">Question 5: Choix multiple</label>
            <p class="mt-1 text-gray-700">Dans quel contexte la mesure en chimie est-elle cruciale pour la <span class="font-semibold">sécurité alimentaire</span>?</p>
            <ul class="mt-2 space-y-2">
                <li>
                    <div class="flex items-center">
                        <input id="question5_option1" name="question5" type="radio" value="option1" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question5_option1" class="ml-3 block text-sm font-medium text-gray-700">La préparation de solutions pour des expériences en laboratoire</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question5_option2" name="question5" type="radio" value="option2" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question5_option2" class="ml-3 block text-sm font-medium text-gray-700">Le développement de nouveaux matériaux plastiques</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question5_option3" name="question5" type="radio" value="option3" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question5_option3" class="ml-3 block text-sm font-medium text-gray-700">L'analyse des pesticides dans les fruits et légumes</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question5_option4" name="question5" type="radio" value="option4" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question5_option4" class="ml-3 block text-sm font-medium text-gray-700">La synthèse de molécules organiques complexes</label>
                    </div>
                </li>
            </ul>
        </div>

        <div>
            <label for="question6" class="block text-sm font-medium text-gray-700">Question 6: Vrai ou Faux</label>
            <p class="mt-1 text-gray-700">Indiquez si l'affirmation suivante est vraie ou fausse: "Les mesures destructives sont appelées ainsi car elles détruisent toujours l'environnement."</p>
            <select id="question6" name="question6" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
                <option value="true">Vrai</option>
                <option value="false">Faux</option>
            </select>
        </div>

        <div>
            <label for="question7" class="block text-sm font-medium text-gray-700">Question 7: Remplir les blancs</label>
            <p class="mt-1 text-gray-700">La mesure en chimie permet de _________ des substances, de _________ leur quantité et de _________ des réactions chimiques.</p>
            <input type="text" id="question7_1" name="question7_1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Premier blanc">
            <input type="text" id="question7_2" name="question7_2" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Deuxième blanc">
             <input type="text" id="question7_3" name="question7_3" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Troisième blanc">
        </div>

        <div>
            <label for="question8" class="block text-sm font-medium text-gray-700">Question 8: Réponse courte</label>
            <p class="mt-1 text-gray-700">Quelle est la différence principale entre une mesure précise et une mesure approximative en termes de matériel utilisé?</p>
            <textarea id="question8" name="question8" rows="2" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Votre réponse"></textarea>
        </div>

        <div>
            <label for="question9" class="block text-sm font-medium text-gray-700">Question 9: Choix multiple</label>
            <p class="mt-1 text-gray-700">Lequel des objectifs suivants de la mesure en chimie est le plus important pour le développement de nouvelles technologies?</p>
            <ul class="mt-2 space-y-2">
                <li>
                    <div class="flex items-center">
                        <input id="question9_option1" name="question9" type="radio" value="option1" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question9_option1" class="ml-3 block text-sm font-medium text-gray-700">Informer les étudiants</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question9_option2" name="question9" type="radio" value="option2" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question9_option2" class="ml-3 block text-sm font-medium text-gray-700">Contrôler les erreurs expérimentales</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question9_option3" name="question9" type="radio" value="option3" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question9_option3" class="ml-3 block text-sm font-medium text-gray-700">Identifier et quantifier de nouvelles substances</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question9_option4" name="question9" type="radio" value="option4" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question9_option4" class="ml-3 block text-sm font-medium text-gray-700">Surveiller la météo</label>
                    </div>
                </li>
            </ul>
        </div>

        <div>
            <label for="question10" class="block text-sm font-medium text-gray-700">Question 10: Question ouverte</label>
            <p class="mt-1 text-gray-700">Comment l'évolution des techniques de mesure a-t-elle façonné notre compréhension de la chimie au fil du temps?</p>
            <textarea id="question10" name="question10" rows="3" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Votre réponse"></textarea>
        </div>

         <div>
            <label for="question11" class="block text-sm font-medium text-gray-700">Question 11: Choix multiple</label>
            <p class="mt-1 text-gray-700">Quel type de mesure est le plus approprié pour assurer un suivi <span class="font-semibold">en temps réel</span> de la concentration d'un produit dans une chaîne de production industrielle?</p>
            <ul class="mt-2 space-y-2">
                <li>
                    <div class="flex items-center">
                        <input id="question11_option1" name="question11" type="radio" value="option1" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question11_option1" class="ml-3 block text-sm font-medium text-gray-700">Mesure unique et précise en laboratoire</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question11_option2" name="question11" type="radio" value="option2" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question11_option2" class="ml-3 block text-sm font-medium text-gray-700">Mesure temporaire par prélèvement d'échantillons</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question11_option3" name="question11" type="radio" value="option3" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question11_option3" class="ml-3 block text-sm font-medium text-gray-700">Mesure continue en ligne</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question11_option4" name="question11" type="radio" value="option4" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question11_option4" class="ml-3 block text-sm font-medium text-gray-700">Mesure destructive finale sur le produit</label>
                    </div>
                </li>
            </ul>
        </div>

        <div>
            <label for="question12" class="block text-sm font-medium text-gray-700">Question 12: Vrai ou Faux</label>
            <p class="mt-1 text-gray-700">Indiquez si l'affirmation suivante est vraie ou fausse: "Le choix de la technique de mesure en chimie est totalement indépendant de la quantité d'échantillon disponible."</p>
            <select id="question12" name="question12" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
                <option value="true">Vrai</option>
                <option value="false">Faux</option>
            </select>
        </div>

        <div>
            <label for="question13" class="block text-sm font-medium text-gray-700">Question 13: Remplir les blancs</label>
            <p class="mt-1 text-gray-700">La concentration _________ est exprimée en g/L, tandis que la concentration _________ est exprimée en mol/L.</p>
            <input type="text" id="question13_1" name="question13_1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Premier blanc">
            <input type="text" id="question13_2" name="question13_2" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Deuxième blanc">
        </div>

        <div>
            <label for="question14" class="block text-sm font-medium text-gray-700">Question 14: Réponse courte</label>
            <p class="mt-1 text-gray-700">Expliquez pourquoi la mesure du pH est cruciale dans le domaine de l'agriculture.</p>
            <textarea id="question14" name="question14" rows="2" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Votre réponse"></textarea>
        </div>

        <div>
            <label for="question15" class="block text-sm font-medium text-gray-700">Question 15: Choix multiple</label>
            <p class="mt-1 text-gray-700">Lequel de ces instruments est utilisé pour effectuer une mesure <span class="font-semibold">temporaire</span> de la qualité de l'eau?</p>
            <ul class="mt-2 space-y-2">
                <li>
                    <div class="flex items-center">
                        <input id="question15_option1" name="question15" type="radio" value="option1" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question15_option1" class="ml-3 block text-sm font-medium text-gray-700">Sondes de pH immergées en continu</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question15_option2" name="question15" type="radio" value="option2" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question15_option2" class="ml-3 block text-sm font-medium text-gray-700">Kits de test colorimétriques</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question15_option3" name="question15" type="radio" value="option3" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question15_option3" class="ml-3 block text-sm font-medium text-gray-700">Analyseurs automatiques en station d'épuration</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question15_option4" name="question15" type="radio" value="option4" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question15_option4" class="ml-3 block text-sm font-medium text-gray-700">Capteurs de pollution atmosphérique</label>
                    </div>
                </li>
            </ul>
        </div>

        <div>
            <label for="question16" class="block text-sm font-medium text-gray-700">Question 16: Vrai ou Faux</label>
            <p class="mt-1 text-gray-700">Indiquez si l'affirmation suivante est vraie ou fausse: "Le choix entre une mesure destructive et non destructive n'a pas d'incidence sur le coût de l'analyse."</p>
            <select id="question16" name="question16" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
                <option value="true">Vrai</option>
                <option value="false">Faux</option>
            </select>
        </div>

        <div>
            <label for="question17" class="block text-sm font-medium text-gray-700">Question 17: Remplir les blancs</label>
            <p class="mt-1 text-gray-700">La mesure en chimie permet de passer d'une approche _________ de la description du monde à une approche _________ et _________.</p>
            <input type="text" id="question17_1" name="question17_1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Premier blanc">
            <input type="text" id="question17_2" name="question17_2" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Deuxième blanc">
             <input type="text" id="question17_3" name="question17_3" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Troisième blanc">
        </div>

        <div>
            <label for="question18" class="block text-sm font-medium text-gray-700">Question 18: Réponse courte</label>
            <p class="mt-1 text-gray-700">Comment les progrès technologiques ont-ils influencé les techniques de mesure en chimie, en particulier en termes de précision et de rapidité?</p>
            <textarea id="question18" name="question18" rows="2" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Votre réponse"></textarea>
        </div>

        <div>
            <label for="question19" class="block text-sm font-medium text-gray-700">Question 19: Choix multiple</label>
            <p class="mt-1 text-gray-700">Lequel de ces objectifs de la mesure en chimie est le plus directement lié à l'amélioration des procédés industriels?</p>
            <ul class="mt-2 space-y-2">
                <li>
                    <div class="flex items-center">
                        <input id="question19_option1" name="question19" type="radio" value="option1" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question19_option1" class="ml-3 block text-sm font-medium text-gray-700">Informer le grand public sur les risques chimiques</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question19_option2" name="question19" type="radio" value="option2" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question19_option2" class="ml-3 block text-sm font-medium text-gray-700">Contrôler et surveiller les réactions</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question19_option3" name="question19" type="radio" value="option3" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question19_option3" class="ml-3 block text-sm font-medium text-gray-700">Identifier les composants d'un produit naturel</label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="question19_option4" name="question19" type="radio" value="option4" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500">
                        <label for="question19_option4" class="ml-3 block text-sm font-medium text-gray-700">Quantifier la pollution des sols</label>
                    </div>
                </li>
            </ul>
        </div>

        <div>
            <label for="question20" class="block text-sm font-medium text-gray-700">Question 20: Question ouverte</label>
            <p class="mt-1 text-gray-700">Si vous deviez expliquer à une personne non scientifique l'importance de la mesure en chimie, quels arguments utiliseriez-vous pour la convaincre?</p>
            <textarea id="question20" name="question20" rows="3" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="Votre réponse"></textarea>
        </div>

        <button type="submit" class="bg-green-700 hover:bg-blue-900 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Envoyer
        </button>
    </form>
    '''

    # Get the updated form with unique IDs
    updated_form_html = update_form_with_unique_ids(form_html)

    # Print the updated form
    print(updated_form_html)


    content_with_time_tag = '''
        <div class="p-4">
        <p class="text-gray-800 text-xl font-semibold mb-4">
            أنا آسف على التكرار، يبدو أنني لم أستوعب سؤالك بشكل صحيح في المرة الأولى.
        </p>
        <p class="text-gray-700 mb-2">
            النظام شبه المعزول (système pseudo-isolé) <span class="font-semibold">لا يمكن أن يغير حالته الحركية من تلقاء نفسه</span>. هذا يعني أنه:
        </p>
        <ul class="list-disc list-inside text-gray-700">
            <li>
                إذا كان في حالة <span class="font-semibold">حركة مستقيمة منتظمة</span>، فإنه سيستمر في هذه الحركة إلى الأبد، ما لم تؤثر عليه قوة خارجية.
            </li>
            <li>
                إذا كان في حالة <span class="font-semibold">سكون</span>، فإنه سيظل ساكناً إلى الأبد، ما لم تؤثر عليه قوة خارجية.
            </li>
        </ul>
        <p class="text-gray-700 mb-2">
            لذا، لا يمكن للنظام شبه المعزول أن "يختار" بين الحركة المستقيمة المنتظمة والسكون. حالته الحركية تحددها سرعته الابتدائية، ويبقى عليها ما لم تتغير الظروف الخارجية.
        </p>
        <p class="text-gray-700 mb-2">
            هل هذا التوضيح أفضل؟
        </p>
        </div><br><time>2025-02-23T15:46:19.977325+00:00</time>
    '''

    # Update the time attribute in the time tag
    updated_content = update_time_in_time_tag(content_with_time_tag, 'wqkdjqwdkqw')
    print(updated_content)
