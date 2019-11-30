def cofiCostFunc(params, Y, R, num_users, num_movies, ... num_features, lam):


	#COFICOSTFUNC Collaborative filtering cost function
	#   [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, ...
	#   num_features, lambda) returns the cost and gradient for the
	#   collaborative filtering problem.
	#

	# Unfold the U and W matrices from params
	X = reshape(params(1:num_movies*num_features), num_movies, num_features);
	Theta = reshape(params(num_movies*num_features+1:end), ...
	                num_users, num_features);

	            
	# You need to return the following values correctly
	J = 0;
	X_grad = zeros(size(X));
	Theta_grad = zeros(size(Theta));

	# ====================== YOUR CODE HERE ======================
	# Compute the cost function and gradient for collaborative
	# filtering. Concretely, you should first implement the cost
	# function (without regularization) and make sure it is
	# matches our costs. After that, you should implement the 
	# gradient and use the checkCostFunction routine to check
	# that the gradient is correct. Finally, you should implement
	# regularization.
	#
	#
	# You should set the following variables correctly:
	#        X_grad - num_movies x num_features matrix, containing the 
	#                 partial derivatives w.r.t. to each element of X
	#        Theta_grad - num_users x num_features matrix, containing the 
	#                     partial derivatives w.r.t. to each element of Theta
	#


	errors = (X*Theta.transpose() - Y) .* R;
	regularizationTheta = lam/2 * sum(sum(Theta.^2));
	regularizationX = lam/2 * sum(sum(X.^2));

	J = 1/2 * sum(sum(errors .^2)) + regularizationTheta + regularizationX;
	X_grad = errors * Theta + lam * X;
	Theta_grad = errors.transpose() * X + lam * Theta


	# =============================================================

	grad = [X_grad(:); Theta_grad(:)]

	return J, grad

