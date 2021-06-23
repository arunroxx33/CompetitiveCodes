#include <bits/stdc++.h>
using namespace std;

// #define int long long
class Node{
	public:
	int leftvalue,rightvalue,val = 0;
	Node *left,*right;
	
	Node(int l,int r){
		leftvalue = l,rightvalue = r;
		left = right = NULL;
	}
};



class SegmentTree{
    public:
	Node *root = NULL;							//SEGMENT TREE ROOT NODE
    
    //INORDER HELPER FUNCTION
    void showinorder(Node *p){
		if(p!=NULL){
			showinorder(p->left);
			cout<<p->val<<" LEFT VALUE"<<p->leftvalue<<" RIGHT VALUE"<<p->rightvalue<<endl;
			showinorder(p->right);
		}
	}

	//SHOW TREE IN INORDER FORM
    void show(){
        showinorder(root);
    }
    
	//BUILD SEGMENT TREE HELPER FUNCITON
	Node* build(vector <int> &nums,int l,int r){
		Node *temp = new Node(l,r);
		if(l == r){
			temp->val = nums[l];
		}
		else
		{
			int mid = (l+r)>>1;
			temp->left = build(nums,l,mid);
			temp->right = build(nums,mid+1,r);
			temp->val = max(temp->right->val,temp->left->val);
		}
		return temp;
	}
	//BUILD SEGMENT TREE
	void buildtree(vector < int>  &nums){
        root =  build(nums,0,nums.size() - 1);
	}

	//UPDATE SEGMENT TREE HELPER FUCNTION
	Node* update(Node* p,int ind,int value){
		if(p->leftvalue == p->rightvalue and p->leftvalue == ind){
			p->val += value;
		}
		else if(p->leftvalue<=ind and p->rightvalue>=ind)
		{
			p->left = update(p->left,ind,value);
			p->right = update(p->right,ind,value);
			p->val = max(p->left->val, p->right->val);
		}
		return p;
		
	}
	//UPDATE SEGMENT TREE
	void updatetree(int ind,int value){
		root = update(root,ind,value);
	}

	//QUERY FUNCTION HELPER
	int query(Node* p,int l,int r){
		if(p->leftvalue>=l and p->rightvalue<=r){ return p->val; }
		else if(p->leftvalue>r or p->rightvalue<l){ return  0;}
		else{ 
			int a = query(p->left,l,r),b = query(p->right,l,r);
			return max(a, b);
		}
	}

	//QUERY FUNCTION
	int queryst(int l,int r){ return query(root,l,r); }
};



signed main(){

}