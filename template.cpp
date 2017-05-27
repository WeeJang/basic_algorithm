#include<iostream>
#include<type_traits>

template<typename T>
using ObjectOf = typename std::remove_reference<typename std::remove_pointer<T>::type>::type;


template<typename F,F f>
struct CallWrapper{
	static void Get() {};		
};

//partital specific template
template<typename T,typename... Args,void(T::*pmf)(Args...)>
struct CallWrapper<void(T::*)(Args...),pmf>{
	static void Invoke(Args... args,void* pobj){
		((reinterpret_cast<T*>(pobj)->*pmf)(args...));	
	}		

	static void (*Get())(){
		return reinterpret_cast<void(*)()>(&Invoke);	
	}

};


#define CALLBACK(POBJ,NAME) \
	CallWrapper<decltype(&ObjectOf<decltype(POBJ)>::NAME),\
			     &ObjectOf<decltype(POBJ)>::NAME>\
	::Get(),static_cast<void*>(POBJ)

//---------------------

struct Callback{
	int context;
	void c_fn(int a,int b){ std::cout << context << " " <<  a << "  " << b << std::endl; }
};



void CallTest(void(*shit)(),void* p_obj){
	auto fn = reinterpret_cast<void(*)(int,int,void*)>(shit);
	fn(1,2,p_obj);	
}


//---------------------

int main(){
	Callback callable{100};
	CallTest(CALLBACK(&callable,c_fn));
	return 0;

}
