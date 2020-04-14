# Two ways of determining the frog problem (boy-girl paradox)

# ALGO1 {
# # Assume population frog_pop with 50% male, 50% female
#
# frog_pair[2] = [random_select(frog_pop), random_select(frog_pop)];
#
# while (frog_pair[0].is_girl() and frog_pair[1].is_girl()) {
# frog_pair = [random_select(frog_pop), random_select(frog_pop)] ;
# }
#
# random_index = random_int(0, 1);
# return frog_pair[random_index].is_girl;
# }
#
# ALGO2 {
# # Assume population frog_pop with 50% male, 50% female
#
# frog_pair[2] = [random_select(frog_pop), random_select(frog_pop)];
# random_index = random_int(0, 1);
#
# while (frog_pair[random_index].is_girl()) {
# frog_pair = [random_select(frog_pop), random_select(frog_pop)];
# random_index = random_int(0, 1);
# }
#
# return frog_pair[1 - random_index].is_girl();
# }